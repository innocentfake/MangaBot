env_vars = {
  # Get From my.telegram.org
  "API_HASH": "33da8f2403e95e6c2504a3c994223c73",
  # Get From my.telegram.org
  "API_ID": "20951184",
  #Get For @BotFather
  "BOT_TOKEN": "8000939036:AAG4QvUuv3F7shFX5EJCJeIdC9rfNWzKuI8",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres:wZNkiy5HDGUnp9uX@frostily-receptive-echidna.data-1.use1.tembo.io:5432/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "fuck_umanga",
  # Force Subs Channel username without @
  "CHANNEL": "Manga_Sect",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "[MS] [{chap_num}] {chap_name} @Manga_Sect",
  # Put Thumb Link 
  "THUMB": "https://github.com/innocentfake/MangaBot/blob/master/thumb.jpg"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
