import snscrape.modules.twitter as sntwitter
import pandas
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import pandas as pd
import nltk
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.tokenize import word_tokenize, RegexpTokenizer

nltk.download('vader_lexicon')
nltk.download('stopwords')

OUTPUT_FILE_NAME = 'data.csv'

async def get_tweets_intoDF(username, tweet_limit):
  sia = SIA()
  df = pd.DataFrame(columns=['neg','neu','pos','compound','label','tweet_text','tweet_date','tweet_replyCount','tweet_retweetCount','tweet_source','tweet_mentionedUsers'])
  #myFile = open('db.txt','w')
  
  for i, tweet in enumerate(sntwitter.TwitterSearchScraper(f'from:{username}').get_items()):
    if i > tweet_limit:
      break
    print(i)
    pol_score = sia.polarity_scores(tweet.rawContent)
    pol_score['tweet_text'] = tweet.rawContent
    label = 0
    if pol_score['compound'] > 0.1:
      label = 1
    elif pol_score['compound'] < -0.1:
      label = -1
    row = [pol_score['neg'],pol_score['neu'],pol_score['pos'],pol_score['compound'],label,tweet.rawContent,(tweet.date).strftime('%m/%d/%Y'),tweet.replyCount,tweet.retweetCount,tweet.source,tweet.mentionedUsers]
    insert_loc = df.index.max()

    if pd.isna(insert_loc):
      df.loc[0] = row
    else:
      df.loc[insert_loc + 1] = row

  await df.to_csv(OUTPUT_FILE_NAME,encoding='utf-8')
  #myFile.close()

def showPercentage():
  df = pd.read_csv('data.csv')
  print(df.label.value_counts(normalize=True)*100)

  fig, ax = plt.subplots(figsize=(8,8))
  #normalize data and count the values 
  cols_to_normalize = ['label']
  distribution = (df[cols_to_normalize].label.value_counts(normalize=True) * 100)
  sns.barplot(x=distribution.index, y=distribution, ax=ax)
  ax.set_xticklabels(['Negative','Neutral','Positive'])
  ax.set_ylabel('Percentage')
  ax.set_title('Distribution of Tweets')
  plt.xticks(rotation=25)
  plt.show()
 


def best(choice):
  df = pd.read_csv('data.csv')
  if (choice == 'positive'):
    bestParagraph = (df['compound'].idxmax())
  else: 
    bestParagraph = (df['compound'].idxmin())
  print(df.at[bestParagraph,'compound'], df.at[bestParagraph, 'tweet_text'])


def process_text(tweet):
  tokenizer =  RegexpTokenizer(r'\w+')
  stop_words = stopwords.words('english')
  lowercase = tweet.lower()
  toks = tokenizer.tokenize(lowercase)
  tokens = []
  for letter in toks:
    if letter not in stop_words:
      tokens.append(letter)
  return tokens
  
def createDict(lines, n):
  tokens = []
  myDict = {}
  for line in lines:
    tokens.extend(process_text(line))
    freq = nltk.FreqDist(tokens)
    most_common = freq.most_common(n)
  for i in range(0, n):
    myDict.update({most_common[i][0]:most_common[i][1]})
  return myDict

def wordCloud(choice):
  _choice = ''
  if (choice == "positive"):
    _choice = 1
  else:
    _choice = -1
  df = pd.read_csv('data.csv')
  lines = list(df[df.label == _choice].tweet_text)
  tokens = []
  for line in lines:
    tokens.extend(process_text(line))
  
  freq = nltk.FreqDist(tokens)
  #print(freq.most_common(20))
  #myWordCloud = wc(background_color="white").generate_from_frequencies(createDict(lines,30))
  #plt.imshow(myWordCloud, interpolation="bilinear")
  #plt.axis("off")
  #plt.show()


# temp = sntwitter.TwitterSearchScraper('from:fadsdafsda').get_items()
# try:
#   enumerate(temp)
# except:
#   print('error')
# for i, tweet in enumerate(temp):
#   print((f'{tweet.user.followersCount:,}'))
  
#   print(f'{tweet.user.friendsCount:,}')
#   print(tweet.user.profileImageUrl)
#   break

# testimonial = TextBlob("Henry says that Henry loves gay people")
# print(testimonial.words.count())
  

#showPercentage()
#wordCloud('negative')
#process_text('@FonsDK We are reaching out to understand more')