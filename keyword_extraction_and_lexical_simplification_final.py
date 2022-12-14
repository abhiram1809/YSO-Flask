# -*- coding: utf-8 -*-
"""Keyword_Extraction and Lexical Simplification (Final).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_ZmAo1XKVI6cmlDBzFNSVtugoMWf4jAF
"""

import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from collections import namedtuple
from nltk import word_tokenize
from functools import lru_cache
import re
import unicodedata
import sys
from collections import Counter
import nltk
from nltk.corpus import brown
from nltk import word_tokenize
from nltk.tokenize import TextTilingTokenizer
from nltk.corpus import stopwords
from nltk import pos_tag


import yake
from heapq import nsmallest
from operator import itemgetter

text = """


Confirmation of Agency Terms in accordance with The Estate Agents Act 1979 and The Estate Agents (Provision of Information) Regulations 1991
  1. Definitions
1.1. “Agreement”, “Agency Agreement” means these Terms of Business and these Terms.
1.2. “Chestertons”, “Us”, “Our” or “We” is Chesterton Global Limited registered
with Companies’ House under number 05334580 and includes its
successors in title.
1.3. “the Property” is the Property as defined in the Terms of Business.
1.4. “the Seller”, “You” or “Your” is the person defined in the Terms of Business as
the Seller/owner of the Property.
1.5. “the Term” means the fixed period overleaf and continues until terminated
in writing by either party as set out in this agreement.
1.6. “the Terms of Business” is the document entitled Terms of Business.
1.7. “Sale Price” includes any part of the price attributable to carpets, curtains
and other fixtures or chattels.
1.8. “VAT” means Value Added Tax or any other replacement or similar tax which
may from time to time be applied to Our fees.
1.9. Commission as set out in the Terms of Business and calculated as the (Sale
Price x Commission Rate) +VAT.
1.10. Consumer means an individual acting for purposes which are wholly or
mainly outside that individual’s trade, business, craft or profession.


2. Agency Type
2.1 Sole Agency – You will be liable to pay remuneration to Us, in addition to any other costs or charges agreed, if at any time unconditional contracts for the sale of the Property are exchanged: With a purchaser introduced by Us during the period of Our Sole Agency or with whom We had negotiations about the Property during that period; or with a purchaser introduced by another agent during that period. Should another agent or body be instructed on the marketing or sale of the Property during the Term then the Agency Agreement will become ‘Multiple Agency’, and the Commission Rate will be the rate applicable to that Agency Type. You may have a dual fee liability in this event.
2.2 Joint Sole Agency – We will be appointed in conjunction with one other agent upon agreement with Us and You. The Commission due under this Agreement will be at the Commission Rate applicable to Joint Sole Agency and the Commission will be divided between Us and the other agent. Should a further or replacement agent be instructed on the marketing or sale of
the Property during the Term without Our prior agreement then the Agency Agreement will become ‘Multiple Agency’ and the Commission Rate will be
the rate applicable to that Agency Type. You may have a dual fee liability in this event.
2.3 Multiple Agency – We will be selling agents at the agreed Commission Rate. During the Term, You may instruct other agents to market and sell the Property. You will be liable to pay remuneration to Chestertons in addition to any other costs or charges agreed, if at any time contracts for the sale of the Property are exchanged with a buyer introduced by Chestertons before termination of the agreement or with whom We had negotiations about the Property during that period. Where a buyer has been introduced by more than one agent, You may have a dual fee liability.


3. Payment of Commission and Late Payments
3.1. Our commission and its rate is as set out in the Terms of Business.
3.2 You are liable to pay Chestertons Commission on a percentage basis and depending upon the Commission Rate for the Agency Type. The Commission will become due on the exchange of contracts for sale of the Property (or absent an exchange, upon completion of a sale); with a buyer during the Term (except in the case of ‘Multiple Agency’), and at any time with a buyer who was introduced to the Property or sale by Us, or with whom We had negotiations on Your behalf during the Term. In the event that there should be a change in the terms of Our instructions such that there is a variation in the rate of Our commission then Our commission will be calculated at the higher rate applicable either at the date of Our introducing the purchaser or the date of exchange of contracts (or absent an exchange, completion of a sale).
3.3 We may defer the payment to be made out of the completion monies at completion of the transaction. By entering into this Agreement, You expressly authorise Your solicitors to pay all Our fees and expenses from the sale proceeds at completion of the transaction and agree that Your solicitors need no further
authority from You in this respect.
3.4 If any sum due to Us is not paid within seven days after it becomes due (normally on completion of the transaction) then We reserve the right to charge interest on it at the rate of 5% above National Westminster Bank PLC base rate from time to time from the date it became due until the date of payment.
3.5 Our commission, any payments due and other agreed expenses also attract VAT at the current rate.
3.6 All reasonable costs of recovery of monies due to Us will be borne by You on an indemnity basis in the event that these are not paid on the due date.


4. Asset Transfer
Where You are a company and shares are sold in addition to or in substitute for a sale of the Property then You will pay Us a sum equivalent to Commission that would have been due under this Agreement if a sale had proceeded through exchange of contracts with Commission falling due at the time of first transfer of shares and based on the total value of all shares transferred in lieu of money for the Property.


5. Continuing Entitlement
You will remain liable to pay Us Our Commission in the event that through another agent You exchange contracts for sale (or absent an exchange, complete a sale) with a party directly or indirectly introduced by Us, or as a result of Our marketing activity within six months of the termination of Our instruction. In the event that there is no other agent involved the time limit extends to twenty-four months.


6. Sub-Agents
We reserve the right, subject to Your consent, to instruct sub-agents on Your behalf where We consider such a step to be in Your best interest. This will involve You in no extra costs and all viewings and negotiations will be coordinated through Us.


7. Energy Performance Certificates (EPCs)
It is a legal requirement to have commissioned an EPC before marketing can commence on your property. Chestertons can arrange an EPC on your behalf at a cost of £60 plus the cost of the EPC. You agree to pay all costs and expenses which We incur in connection with the arrangement of an EPC (whether or not the Term or the Agreement is terminated early, or the Property is sold other than in circumstances where We are entitled to Commission.)


8. Unoccupied Property and Property Security
8.1 We do not accept liability or responsibility for the maintenance or repair of the Property at any time, except caused by Our negligence or default.
8.2 We do not accept responsibility in the event of any damage or loss at the Property, except caused by negligence or default on Our part.
8.3 We do not accept liability for loss of keys beyond the cost of cutting a replacement set.


9. Services to Prospective Purchasers
If a prospective buyer of the Property has a property to sell We reserve the right to act on such a person’s behalf if We are instructed to do so.


10. Referral Fees
Chestertons works with a range of 3rd party service providers that are quality and compliance vetted to ensure that any service the 3rd party contractor may provide meets best practice and legal requirements to complement and support the services we offer to you. Where an existing referral arrangement is in place with the 3rd party service provider, Chestertons may receive a referral fee from the supplier in return for recommending their services to you or prospective buyers where you or prospective buyers decide to take advantage of those services. This referral fee may take the form of a commission, payment, fee or similar reward. You will be consulted in advance of any referral being made to a 3rd party service provider and the potential referral fee will be disclosed to you so that you can make an informed decision about whether to proceed with our recommended service provider. The referral fee we receive will not affect the final amount you pay to the 3rd party service provider, nor will it impact upon your obligation to pay Chestertons fees where applicable.
  Chestertons TOBs April 2021
Initial....................
DocuSign Envelope ID: C6FBBBA5-A538-46F6-90AB-3E404769F498
  Sales Terms of Business


11. The Money Laundering, Terrorist Financing and Transfer of Funds (Information on the Payer) Regulations 2017
Chestertons operates a strict policy of complying at all times with Money Laundering Regulations and in particular the Proceeds of Crime Act 2002.
If You are not prepared to comply with Our policy and procedures, then We reserve the right to refuse to act for You or to decline to act further, without waiver of any sums We are entitled to under this Agreement. Chestertons
may conduct an electronic identity check on You, or each of You if more than one, and on all beneficiaries of organisations for the purpose of the Money Laundering Regulations 2017. The electronic anti-money laundering check will be conducted by NorthRow Ltd, 33 Upper High Street, Thame, Oxfordshire, OX9 3EZ. In signing this agreement, You hereby consent to this check being conducted. In the event where an electronic check is not possible, You, or each of You if more than one, will be asked to provide two separate items of identity evidence in the form of:
  Proof of photographic identity e.g. original driving license or passport
  Proof of current residential address e.g. a recent utility bill dated in the last 3 months
Where You are an incorporated or other legal entity, You will be asked to provide the following:
 Evidence to verify the legal existence of the company or organisation e.g.
Memorandum & Articles of Incorporation
 Evidence and proof of identity of the beneficial owner(s) with an interest of
25% or greater
 Evidence of the organisation’s directors
 Confirmation that the person acting on Your behalf is authorised to do so.
Copies of the above will be held for a minimum period of five years after the completion of Your business with Us. We reserve the right to stop acting for
You if such is not provided as soon as practicable on request. Should We receive information which gives rise to suspicions of Money Laundering (including deliberate non-declaration of income to HMRC (Her Majesty’s Revenue and Customs)) or similar unlawful activity, We will be required under the Proceeds of Crime Act 2002, and related regulations, to make a report to the NCA (National Crime Agency) who may refer the matter on then to the law enforcement agencies. Please note that this act overrides Our duty of client confidentiality and may also involve the transfer of data outside the European Economic Area.


12. The General Data Protection Regulation (EU) 2016/679 (“GDPR”) and the Data Protection Act 2018
You hereby consent to Us processing data or supplying to third parties any information, or personal details on You as defined in the GDPR and the Data Protection Act 2018 for the performance of this contract. This means We
may disclose such information on You to other agents or suppliers of services, solicitors, mortgage brokers or potential mortgagors where there is a legitimate interest to do so. Chestertons will only use Your personal information in accordance with Our Privacy Policy. We will record and retain sensitive personal data and You are entitled to request a copy of all data held about you and to have the same amended if found to be incorrect. Further details can be found at www.chestertons.com/about-us/privacy-and-cookies or which can be provided upon request.


13. Copyright
We retain copyright in and ownership of all documents, drawings, maps, reports, photographic and other records produced by Us, including this Agreement, in connection with Our work for You.


14. Jurisdiction
The High Court and the County Courts of England and Wales shall have jurisdiction over this agreement.


15. Entire agreement, variations and termination of agency agreement
15.1 This contract constitutes the entire agreement between Chestertons and the seller and supersedes all prior agreements, understandings, representations or communications between the parties. No amendment or variation to this contract will have any contractual effect unless approved in writing by Us.
15.2 This Agency Agreement will continue until You or We give 21 days’ notice (14 days in the case of a Multiple Agency instruction). Such notice not to be given before the expiry of 16weeks from the date of this Agreement. Following termination of the term you may still be liable for our commission if you sell the property to someone introduced by us.
Chestertons TOBs April 2021


16. Complaints
At Chestertons, we endeavour to provide the highest levels of service. We do however recognise that on occasion things do not go according to plan. In such instances, Chestertons operates an internal complaints procedure. In the first instance, please contact the manager of the office or department concerned. If you are unable to resolve the matter with the branch/department manager and wish to escalate your complaint, please send a summary of your complaint by email to customer.service@chestertons.com or write to: Chestertons, Customer Services, 44-48 Old Brompton Road, South Kensington, London, SW7 3DY.
Following our response If you remain dissatisfied, you are entitled to refer the matter to The Property Ombudsman within twelve months for a review.
We are members of The Property Ombudsman and abide by The Property Ombudsman Code of Practice. You agree that we may disclose information relating to the sale of your property to The Property Ombudsman, if you or the applicant have registered a complaint and The Property Ombudsman asks for
it. You also agree that we may disclose your contact details to The Property Ombudsman if they ask for them, to assist in their monitoring of our compliance with the Code of Practice.


17. Cancellation of Contract under the Consumer Contracts (Information, Cancellation and Additional Charges) Regulation 2013
17.1 Where We are entering into this Agreement with You and You are a Consumer and the contract formed by these Terms of Business is either, what is known as an ‘Off-Premises Contract’ or a ‘Distance Contract’, You may have the right to cancel these Terms of Business without giving any reason within 14 days from the day you entered into them.
17.2 If You require the early commencement of Our services, You will become liable for Our fees as set out in these Terms of Business.
17.3 If You do ask Us to commence services and You later cancel (during the cancellation period) You may be liable for Our fees in connection with the performance of those services, which may include Our fees in proportion to the services which We provide until the conclusion of the agreement.
17.4 If, in the cancellation period, we have made introductions that result in the sale of the Property Your right to cancel may be lost as We may have completed the terms of Our retainer and Our fees may be payable in full.
17.5 To exercise Your right to cancel the contract within the 14-day period You must inform Us in writing of Your decision to cancel this contract. You may do so by letter sent by post to Chestertons of 40 Connaught Street, Hyde Park, London, W2 2AB or by email to cancellation@chestertons.com. A cancellation form is attached which You may wish to use but You are not obliged to do so.
If You wish to cancel the contract within the 14-day period described above. You may use this form if You want to but You do not have to. (Complete and return this form only if you wish to cancel the contract)

TO: Chestertons of
40 Connaught Street, Hyde Park, London, W2 2AB
I/We hereby give notice that I/We wish to cancel My/Our contract with Chestertons relating to:
Property Address:
Name:
Address:
Signature:


"""

"""# **Summarization**"""

#text = re.sub(r'\d.\d|\d\d.','',text)
#print(text)


import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize,word_tokenize
from gensim.models import Word2Vec
import numpy as np
import re

def remove_special_characters(text): # used
    regex = r'[^a-zA-Z0-9\s]'
    text = re.sub(regex,'',text)
    regex = r'(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)'
    text = re.sub(regex,'',text)
    return text

def paragraph_cleaner(tokens): # used
    tokens_cleaned = []
    for token in tokens:
        token = remove_special_characters(token)
        tokens_cleaned.append(token)
    return tokens_cleaned


def checkNum(s):
    l= ['1','2','3','4','5','6','7','8','9','0']
    check =False

    for i in s:
        if i in l:
            check = True
            break
    if check == True:
        return 1
    else:
        return 0

def meanOfWord(model_word, paragraph):
    posList=['CD']
    nounList=['NN','NNP','NNS','NNPS']
    value=[]
    count=0
    noun=0
    for word in paragraph:
        a=model_word.wv.most_similar(word)
        temp=[]
        for w in a:
            temp.append(w[1])
        posValue=nltk.pos_tag([word])
        wordScore=np.mean(temp)
        if posValue[0][1] in posList:
            count=count+1
        else:
            valueIfNum=checkNum(word)
            count=count+valueIfNum
        if posValue[0][1] in nounList:
            noun=noun + .25
        value.append(wordScore)
    return np.mean(value)+count+noun














def relevant_text_ranker(n,sorted_tokens):
  relevant_text = []
  if(n==1):
    for i in range(5):
      relevant_text.append(sorted_tokens[i][0])
  if(n==2):
    if len(sorted_tokens)>20:
      for i in range(20):
        relevant_text.append(sorted_tokens[i][0])
    else:
      for i in range(len(sorted_tokens)):
        relevant_text.append(sorted_tokens[i][0])
  if(n==3):
    points = len(sorted_tokens)
    for i in range(points):
      relevant_text.append(sorted_tokens[i][0])
    return relevant_text
  return relevant_text





import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
nlp= spacy.load("en_core_web_sm")
from heapq import nlargest
import transformers
from transformers import pipeline

"""# **Grammatical Correctness**"""


#import language_tool_python
from happytransformer import HappyTextToText
from happytransformer import TTSettings

happy_tt = HappyTextToText("T5",  "prithivida/grammar_error_correcter_v1", use_auth_token = "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")
#tool = language_tool_python.LanguageTool('en-US')
#def grammar_corrector(text):
  #matches = tool.check(text)
  #my_mistakes = []
  #my_corrections = []
  #start_positions = []
  #end_positions = []
  
  #for rules in matches:
      #if len(rules.replacements)>0:
          #start_positions.append(rules.offset)
          #end_positions.append(rules.errorLength+rules.offset)
          #my_mistakes.append(text[rules.offset:rules.errorLength+rules.offset])
          #my_corrections.append(rules.replacements[0])
      
  
      
  #my_new_text = list(text)
  
  
  #for m in range(len(start_positions)):
      #for i in range(len(text)):
          #my_new_text[start_positions[m]] = my_corrections[m]
          #if (i>start_positions[m] and i<end_positions[m]):
              #my_new_text[i]=""
      
  #my_new_text = "".join(my_new_text)
  #return(my_new_text)
def grammar_corrector_2(text):
   settings = TTSettings(do_sample=True, top_k=0, temperature=0.7,  min_length=1, max_length=1000)
   result = happy_tt.generate_text(text, args=settings)
   return result.text


def listToString(s): 
    str1 = " " 
    return (str1.join(s))

def listToString2(s): 
    str1 = "" 
    return (str1.join(s))

"""# **Keyword Extraction**"""

simple_kwextractor = yake.KeywordExtractor()

#for kw in keywords:
	#print(kw)
def free_user(extracted_keywords):
  return_phrases = []
  free_user_phrases = nsmallest(5, extracted_keywords, key=itemgetter(1)) #Lower Score means Higher Relevance
  for phrase,score in free_user_phrases:
    return_phrases.append(phrase)
  return return_phrases



def premium_user(extracted_keywords):
  return_phrases = []
  premium_user_phrases = nsmallest(20, extracted_keywords, key=itemgetter(1)) #Lower Score means Higher Relevance
  for phrase,score in premium_user_phrases:
    return_phrases.append(phrase)
  return return_phrases


def business_account_user(extracted_keywords):
  return_phrases = []
  business_user_input = int(input())
  business_user_phrases = nsmallest(business_user_input, extracted_keywords, key=itemgetter(1)) #Lower Score means Higher Relevance
  for phrase,score in business_user_phrases:
    return_phrases.append(phrase)
  return return_phrases



def text_summarizer_free(text):
  summarizer = pipeline("summarization")
  summarized = summarizer(text,  truncation=True)
  summ=' '.join([str(i) for i in summarized])
  summ=summ.replace("{","")
  summ=summ.replace("''","")
  return summ[18:-2]
def text_summarizer_premium(text):
  summarizer = pipeline("summarization")
  summarized = summarizer(text,  truncation=True)
  summ=' '.join([str(i) for i in summarized])
  return summ[18:-2]
def text_summarizer_business(text):
  summarizer = pipeline("summarization")  
  summarized = summarizer(text)
  summ=' '.join([str(i) for i in summarized])
  summ=summ.replace("{","")
  summ=summ.replace("''","")
  return summ[18:-2]



def final_function (user, text_list, business_phrases):
  rel_list=[]
  grave = ''
  if(user == 1):
    for relevance in text_list[0]:
      rel_list = []
      if (len(relevance.split())<24):
        relevance = relevance.replace('\n','')
        rel_list.append(relevance)
      else:
        for sentence in sent_tokenize(text_summarizer_free(relevance)):
          if(len(sentence.split())<6 or list(sentence)[0].isupper() == False):
            pass
          else:  
            correct_sentence = grammar_corrector_2(sentence)
            rel_list.append(correct_sentence)
      grave += "*" + listToString(rel_list) + "\n"
  if(user == 2):
    for relevance in text_list[1]:
      rel_list = []
      if (len(relevance.split())<24):
        relevance = relevance.replace('\n','')
        rel_list.append(relevance)
      else:
        for sentence in sent_tokenize(text_summarizer_free(relevance)):
          if(len(sentence.split())<6 or list(sentence)[0].isupper() == False):
            pass
          else:  
            correct_sentence = grammar_corrector_2(sentence)
            rel_list.append(correct_sentence)
      grave += "*" + listToString(rel_list) + "\n"
  if(user == 3):
    print("The Keywords for given subtopics are as follows:")
    for bullet_number, phrase_text in enumerate(business_phrases):
        print(str(bullet_number + 1) + ". "+ phrase_text[0] + "," + phrase_text[1] + "\n")
    bullet_inputs = []
    print("Enter the bullet points you want for text:")
    while True:
      tempo = str(input())
      if (tempo) == "":
        break
      bullet_inputs.append(text_list[2][int(tempo)-1])
    for relevance in bullet_inputs:
      rel_list = []
      if (len(relevance.split())<24):
        relevance = relevance.replace('\n','')
        rel_list.append(relevance)
      else:
        for sentence in sent_tokenize(text_summarizer_free(relevance)):
          if(len(sentence.split())<6 or list(sentence)[0].isupper() == False):
            pass
          else:  
            correct_sentence = grammar_corrector_2(sentence)
            rel_list.append(correct_sentence)
      grave += "*" + listToString(rel_list) + "\n"
  return user,grave






def full_function_in_one_package(user, text):
  ttt = nltk.tokenize.TextTilingTokenizer(w=20)
  tokens = ttt.tokenize(text)
  tokenized_paragraphs = paragraph_cleaner(tokens)
  model_word = Word2Vec(tokenized_paragraphs, min_count=1,sg=1)
  score=[]
  for index, sentence in enumerate(tokenized_paragraphs):
    i = tokenized_paragraphs.index(sentence)
    meanScore= meanOfWord(model_word,sentence)
    temp = [i,meanScore]
    score.append(temp)
  important_keyphrases = ['ip address', 'mobile carrier','device ids','use of data','device activity','activity across devices', 'platform’s messaging functionality','disclose messages','remuneration','payment']
  token_scores = []
  for scores in score:
    token_scores.append(scores[1])
  sorted_tokens = list(zip(tokens,token_scores))  
  temp_list = []
  for tuples in sorted_tokens:
    tuple_as_list = list(tuples)
    for phrases in important_keyphrases:
      if(tuple_as_list[0].lower().find(phrases)!=-1):
        tuple_as_list[1] = 570
    temp_list.append(tuple_as_list)
  sorted_tokens = temp_list
  sorted_tokens.sort(key= lambda a:a[1], reverse=1)
  relevant_text_free = relevant_text_ranker(1,sorted_tokens)
  relevant_text_premium = relevant_text_ranker(2,sorted_tokens)
  relevant_text_business = relevant_text_ranker(3,sorted_tokens)
  all_phrases = []
  for texto in relevant_text_business:
      keywords = simple_kwextractor.extract_keywords(texto)
      business_user_phrases = nsmallest(2, keywords, key=itemgetter(1))
      text_phrase = []
      for phrase,score in business_user_phrases:
         text_phrase.append(phrase)
      all_phrases.append(text_phrase)
  text_list = [relevant_text_free, relevant_text_premium, relevant_text_business]
  User,Output = final_function(user, text_list, all_phrases)
  return User, Output
"""# **Document Generation**"""
def Doc_generator(User,Output,path):
  if (User == 1):
    with open('{}'.format(path)+'Free_User'+'.txt', 'w', encoding="utf-8") as f:
        f.write(Output) 
  if (User == 2):
    with open('{}'.format(path)+'Premium_User'+'.txt', 'w', encoding="utf-8") as f:
        f.write(Output)
  if (User == 3):
    with open('{}'.format(path)+'Business_User'+'.txt', 'w', encoding="utf-8") as f:
        f.write(Output)


def Business_User_Point_Extraction(text):
  ttt = nltk.tokenize.TextTilingTokenizer(w=20)
  tokens = ttt.tokenize(text)
  tokenized_paragraphs = paragraph_cleaner(tokens)
  model_word = Word2Vec(tokenized_paragraphs, min_count=1,sg=1)
  score=[]
  for index, sentence in enumerate(tokenized_paragraphs):
    i = tokenized_paragraphs.index(sentence)
    meanScore= meanOfWord(model_word,sentence)
    temp = [i,meanScore]
    score.append(temp)
  important_keyphrases = ['ip address', 'mobile carrier','device ids','use of data','device activity','activity across devices', 'platform’s messaging functionality','disclose messages','remuneration','payment']
  token_scores = []
  for scores in score:
    token_scores.append(scores[1])
  sorted_tokens = list(zip(tokens,token_scores))  
  temp_list = []
  for tuples in sorted_tokens:
    tuple_as_list = list(tuples)
    for phrases in important_keyphrases:
      if(tuple_as_list[0].lower().find(phrases)!=-1):
        tuple_as_list[1] = 570
    temp_list.append(tuple_as_list)
  sorted_tokens = temp_list
  sorted_tokens.sort(key= lambda a:a[1], reverse=1)
  relevant_text_business = relevant_text_ranker(3,sorted_tokens)
  all_phrases = []
  for texto in relevant_text_business:
      keywords = simple_kwextractor.extract_keywords(texto)
      business_user_phrases = nsmallest(2, keywords, key=itemgetter(1))
      text_phrase = []
      for phrase,score in business_user_phrases:
         text_phrase.append(phrase)
      all_phrases.append(text_phrase)
  return all_phrases, relevant_text_business

def ff_Business_User(Bullets, relevant_text_business):
  bullet_inputs = []
  grave = ''
  for Bullet in Bullets:
    bullet_inputs.append(relevant_text_business[Bullet][0])
  for relevance in bullet_inputs:
    rel_list = []
    if (len(relevance.split())<24):
      relevance = relevance.replace('\n','')
      rel_list.append(relevance)
    else:
      for sentence in sent_tokenize(text_summarizer_free(relevance)):
        if(len(sentence.split())<6 or list(sentence)[0].isupper() == False):
          pass
        else:  
          correct_sentence = grammar_corrector_2(sentence)
          rel_list.append(correct_sentence)
    grave += "*" + listToString(rel_list) + "\n"
  return 3, grave 