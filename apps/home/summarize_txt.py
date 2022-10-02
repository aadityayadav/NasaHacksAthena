import inflect
from transformers import pipeline
import os
from wordwise import Extractor
import re
from apps.home.pdfEx import process_pdf
# from run import buildModel
import json
import requests
import string

def generateTxt(filename):
  text = process_pdf(filename)
  
  # ## Setting to use the 0th GPU
  os.environ["CUDA_VISIBLE_DEVICES"] = "0"

  try:
    text = text[text.index("Abstract"):]
    text = text[:text.index("Introduction")]
  except:
    text = text

  try:
    text = text[text.index("ABSTRACT"):]
    text = text[:text.index("INTRODUCTION")]
  except:
    text = text
  # text = text[:text.index("The SocketManager")]
  # summarizer = buildModel()
    
  # print(text)
  
  # print(summary_text)


  
  API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-xsum"
  token = "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"
  headers = {"Authorization": f"Bearer {token}"}

  def query(payload):
      data = json.dumps(payload)
      response = requests.request("POST", API_URL, headers=headers, data=data)
      return json.loads(response.content.decode("utf-8"))
  summary_text = query(
    {
      "inputs": text,
      "parameters": {"max_length": 300, "min_length": 200,"do_sample": False}
    }
  )
  # print(summary_text)

  try:
    summary_text = summary_text[0]['summary_text']
  except:
    summary_text = summary_text

  try:
    summary_text = summary_text.dict('summary_text')
  except:
    summary_text = summary_text

  # try:
  #   summary_text = summary_text[:summary_text.index("[1,2,3")]
  # except: 
  #   summary_text = summary_text
    
  extractor = Extractor()
  keywords = extractor.generate(summary_text, 5)

  p = inflect.engine()
  for word in keywords:
    if p.plural(word) in keywords:
      keywords.remove(p.plural(word))

  summary_text = ''.join([str(char) for char in summary_text if char in string.printable])

  return summary_text, keywords