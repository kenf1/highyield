#import modules
import pyttsx3
import pandas as pd

#spreadsheet_tts    
def spreadsheet_tts(file_name,lower_bound=0,upper_bound=None,header=None):
    """Text-to-speech from rows in specified spreadsheet (`.csv` or `.xls*`) file. By default, the function will use all rows from the specified spreadsheet.

    Args:
        file_name (str): Full path to spreadsheet file. Will see error if file doesn't match either format.
        lower_bound (int, optional): Which row should TTS engine start from? Defaults to 0 (first row).
        upper_bound (int, optional): Which row should TTS engine end? Defaults to None (last row).
        header (str, optional): Does header exist in spreadsheet file? Defaults to None.
    """
    
    #will choose whether to use read_csv or read_excel, throws error if either can't read+import
    try:
        raw_text = pd.read_csv(filepath_or_buffer=file_name,header=header)
    except:
        raw_text = pd.read_excel(io=file_name,header=header)

    #rm NaN rows
    raw_text = raw_text.dropna()
    
    #convert df col to list
    if upper_bound is None:
        text = raw_text[0].tolist()[lower_bound:]
    else:
        text = raw_text[0].tolist()[lower_bound:upper_bound]
    
    engine = pyttsx3.init()

    #TTS for selected rows
    for text in text:
        engine.say(text=text)
    engine.runAndWait()

#spreadsheet_tts_save
def spreadsheet_tts_save(file_name,save_name,lower_bound=0,upper_bound=None,header=None):
    """Saves text-to-speech output from rows in specified spreadsheet (`.csv` or `.xls*`) file. Similar to `spreadsheet_tts` but saves output instead. By default, the function will use all rows from the specified spreadsheet.

    Args:
        file_name (str): Full path to spreadsheet file. Will see error if file doesn't match either format.
        save_name (str): Full path and extension for audio file output from this function.
        lower_bound (int, optional): Which row should TTS engine start from? Defaults to 0 (first row).
        upper_bound (int, optional): Which row should TTS engine end? Defaults to None (last row).
        header (str, optional): Does header exist in spreadsheet file? Defaults to None.
    """
    
    #will choose whether to use read_csv or read_excel, throws error if either can't read+import
    try:
        raw_text = pd.read_csv(filepath_or_buffer=file_name,header=header)
    except:
        raw_text = pd.read_excel(io=file_name,header=header)

    #rm NaN rows
    raw_text = raw_text.dropna()
    
    #convert df col to list
    if upper_bound == None:
        text = raw_text[0].tolist()[lower_bound:]
    else:
        text = raw_text[0].tolist()[lower_bound:upper_bound]
    
    #convert list to single string w/ space between each item
    text = " ".join(text)

    engine = pyttsx3.init()

    #TTS for selected rows
    engine.save_to_file(text=text,filename=save_name)
    engine.runAndWait()
    
#df_tts
def df_tts(df_name,lower_bound=0,upper_bound=None):
    """Text to speech from user imported dataframe. By default, the function will use all rows from the specified spreadsheet.

    Args:
        df_name (str): Name of dataframe to pass into this function.
        lower_bound (int, optional): Which row should TTS engine start from? Defaults to 0 (first row).
        upper_bound (int, optional): Which row should TTS engine end? Defaults to None (last row).
    """
    
    #rm NaN rows
    raw_text = df_name.dropna()
    
    #convert df col to list
    if upper_bound is None:
        text = raw_text[0].tolist()[lower_bound:]
    else:
        text = raw_text[0].tolist()[lower_bound:upper_bound]
    
    engine = pyttsx3.init()

    #TTS for selected rows
    for text in text:
        engine.say(text=text)
    engine.runAndWait()
    
#df_tts_save
def df_tts_save(df_name,save_name,lower_bound=0,upper_bound=None):
    """Saves text-to speech from user imported dataframe. By default, the function will use all rows from the specified spreadsheet.

    Args:
        df_name (str): Name of dataframe to pass into this function.
        save_name (str): Full path and extension for audio file output from this function.
        lower_bound (int, optional): Which row should TTS engine start from? Defaults to 0 (first row).
        upper_bound (int, optional): Which row should TTS engine end? Defaults to None (last row).
    """
    
    #rm NaN rows
    raw_text = df_name.dropna()
    
    #convert df col to list
    if upper_bound is None:
        text = raw_text[0].tolist()[lower_bound:]
    else:
        text = raw_text[0].tolist()[lower_bound:upper_bound]
    
    #convert list to single string w/ space between each item
    text = " ".join(text)

    engine = pyttsx3.init()

    #TTS for selected rows
    engine.save_to_file(text=text,filename=save_name)
    engine.runAndWait()