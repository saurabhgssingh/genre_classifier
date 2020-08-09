class clean_text():
      def __init__(self, text = "test"):
        self.text = text

      def remove_stopwords(self):
          from nltk.corpus import stopwords
          stop_words = set(stopwords.words('english'))
          no_stopword_text = [w for w in self.text.split() if not w in stop_words]
          self.text = ' '.join(no_stopword_text)
          return self
  
      def clean(self):
          import re 
          # remove backslash-apostrophe 
          txt = re.sub("\'", "", self.text) 
          # remove everything except alphabets 
          txt = re.sub("[^a-zA-Z]"," ",txt) 
          # remove whitespaces 
          txt = ' '.join(txt.split()) 
          # convert text to lowercase 
          self.text = txt.lower() 
          return self
      
      def do_all(self,text):
        self.text = text
        self = self.remove_stopwords()
        self = self.clean()
        return self.text