# Hosting Your Discord Bot on bot-hosting.net

## Files to Upload
When uploading your bot to bot-hosting.net, include these essential files:

1. `bot.py` - Your main bot file
2. `commands/` folder - Contains all your command modules
3. `database_configurations/` folder - Contains database connection code
4. `bot-hosting-requirements.txt` - Rename to `requirements.txt` when uploading

## Configuration Steps

### 1. Create an Account
Sign up for an account on bot-hosting.net

### 2. Create a New Bot
- Click "Create Bot" on your dashboard
- Select "Python" as the language
- Choose the appropriate plan based on your needs

### 3. Upload Your Files
- Use the file manager to upload all your bot files
- Make sure to rename `bot-hosting-requirements.txt` to `requirements.txt`

### 4. Set Environment Variables
Add these essential environment variables in the bot-hosting.net dashboard:
- `DISCORD_TOKEN` - Your Discord bot token
- `DATABASE_URL` - Your PostgreSQL database URL
- Any other secrets your bot uses

### 5. Configure Start Command
Set the start command to: `python bot.py`

### 6. Start Your Bot
Click the "Start" button to launch your bot!

## Troubleshooting
- If your bot fails to start, check the logs for error messages
- Ensure all environment variables are correctly set
- Verify that all required files were uploaded

## Database Configuration
bot-hosting.net supports external databases, so you can continue using your existing PostgreSQL database by providing the correct connection URL in the environment variables.