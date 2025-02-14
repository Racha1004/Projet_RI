import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from transformers import pipeline


def RemoveStopWords(queries):
    """
    Removes all stopwords from the query
    """
    queries_variations= []
    for query in queries :
        query_lower = query.lower()
        tokens = nltk.word_tokenize(query_lower)
        query_without_stop_words = [word for word in tokens if word not in stopwords.words('english')]
        query_without_stop_words = ' '.join(query_without_stop_words)
        queries_variations.append(query_without_stop_words)
    return queries_variations



def T5DescToTitle(queries):
  summarizer = pipeline("summarization", model="/content/gdrive/MyDrive/t5-base_from_description_to_title/", tokenizer="t5-base")

  query_variations = []
  queries_input = ["summarize : {}? </s>".format(query) for query in queries]

  titles = summarizer(queries_input, min_length=3, max_length=8)
  for title in titles:
      query_variations.append(title['summary_text'])
     
  return query_variations
