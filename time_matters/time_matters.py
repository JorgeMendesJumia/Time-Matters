from time_matters.InvertedIndex import kw_ext
from time_matters.GetDateScores import dt_frames
from langdetect import detect
import nltk


def timeMatters(txt, contextual_window_distance=10, threshold=0.05, max_array_len=0, max_keywords=10, analysis_sentence=True):
    #detect language of the text
    lang = detect(txt)
    dictionary, words_array, dates_array = kw_ext(lang, txt, max_keywords)
    relevant_dates = dt_frames(dictionary, words_array, dates_array, contextual_window_distance, threshold, max_array_len, analysis_sentence)

    dates_array_score = []
    for k in range(len(relevant_dates)):
        dates_array_score.append({'Date': relevant_dates[k][0], 'Score': relevant_dates[k][1]})
    return dates_array_score


def timeMattersPerSentence(txt, contextual_window_distance=10, threshold=0.05, max_array_len=0, max_keywords=10, analysis_sentence=True):
    #detect language of the text
    sentences = nltk.sent_tokenize(text)
    dates_array_score = []
    lang = detect(text)
    for i in range(len(sentences)):
        dictionary, words_array, dates_array = kw_ext(lang, sentences[i], max_keywords)
        relevant_dates = dt_frames(dictionary, words_array, dates_array, contextual_window_distance, threshold, max_array_len, analysis_sentence)
        for k in range(len(relevant_dates)):
            dates_array_score.append({'Sentence '+str(i+1): {'Date': relevant_dates[k][0], 'Score': relevant_dates[k][1]}})
    return dates_array_score