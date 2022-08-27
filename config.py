# FILES BELONGS TO @THEDEADLYBOTS 

import os
from dotenv import load_dotenv

# For Local Deploy
if os.path.exists(".env"):
    load_dotenv(".env")

# Necessary Vars
API_ID = int(os.getenv("API_ID", "11482995"))
API_HASH = os.getenv("API_HASH", "3e49c3a642dbfac5e1ae82d287b28ebe")
SESSION = os.getenv("SESSION", "AQDCHMuCAWcYx8NwE3QpGeZYYKeqhJHxBH27xaqyvK6v9jMPKq2mDuBJ4qBj4y2nAQGDccDTEpNzlHnXp8ulglHg271Bc2vzCMUPdz2VtqStUVmAYN89mLO69Wbi_73QZ3Gx34CvorK0Z0Fe1s-o-3_CQSJqcJjJus0lSzlTvVn4ZeXQiuh20aAogFxwUygDolOr42SQxUr0Qr0a_UD5onIIw47hpE_ZJaLnaQfe6jA0LSR4pJQGgHWQvFvyzVeb3zDJwQ5D5o-VkIASOoFl6UFV1fdV71nJ7HNXKeEdfYgvQDgkOzewesPIoY6GMl38b8xGCKjrWLbI6KDz_X3Mz_RFAAAAAUtlt30A")
OWNER = os.getenv("OWNER", "itz_sambodhiraj_xd")
SUPPORT = os.getenv("SUPPORT", "TheDeadlyBots")
SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "5429619191 5466353118").split()))
