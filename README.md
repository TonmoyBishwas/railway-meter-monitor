# 🚂 Railway Electricity Meter Bot

A 24/7 automated electricity meter scraper bot that monitors DESCO prepaid electricity meters and sends balance updates via Telegram. **Optimized specifically for Railway deployment**.

## ✨ Features

- 🔋 **Multi-Meter Monitoring**: Tracks 5 electricity meters simultaneously
- 🤖 **Smart Recharge Detection**: Prevents false low-balance warnings after recharges
- ⏰ **Scheduled Monitoring**: Runs daily at customizable times (default: 8 AM Bangladesh time)
- 📱 **Telegram Notifications**: Instant alerts for low balances (<100 BDT)
- 🚂 **Railway Optimized**: Built for 24/7 operation on Railway platform
- 🔄 **Auto-Recovery**: Automatically restarts if the service crashes
- 🏥 **Health Monitoring**: Built-in health check endpoints

## 🚀 Quick Deploy to Railway

### 1. Prerequisites
- Railway account with Hobby plan ($5/month for 24/7 operation)
- Telegram bot token and chat ID
- DESCO account numbers for your meters

### 2. Deploy Steps

1. **Fork this repository** to your GitHub account

2. **Connect to Railway**:
   - Go to [Railway](https://railway.com)
   - Click "New Project" → "Deploy from GitHub repo"
   - Select this repository

3. **Set Environment Variables** in Railway dashboard:
   ```
   TELEGRAM_BOT_TOKEN=your_telegram_bot_token
   TELEGRAM_CHAT_ID=your_telegram_chat_id
   METER_WEBSITE_URL=https://prepaid.desco.org.bd/customer/#/customer-login
   SCHEDULE_TIMES=08:00
   TEST_RUN=false
   ```

4. **Deploy**: Railway will automatically build and deploy using Docker

## 📱 Getting Telegram Credentials

### Create Telegram Bot:
1. Message [@BotFather](https://t.me/BotFather) on Telegram
2. Send `/newbot` and follow instructions
3. Save the bot token

### Get Chat ID:
1. Send a message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Find your `chat_id` in the response

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Default |
|----------|-------------|----------|---------|
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token | ✅ | - |
| `TELEGRAM_CHAT_ID` | Your Telegram chat ID | ✅ | - |
| `METER_WEBSITE_URL` | DESCO website URL | ❌ | prepaid.desco.org.bd |
| `SCHEDULE_TIMES` | Check times (BD time) | ❌ | 08:00 |
| `TEST_RUN` | Test mode toggle | ❌ | false |
| `PORT` | Health server port | ❌ | 8080 |

### Schedule Times Format
- Single time: `08:00`
- Multiple times: `08:00,20:00` (comma-separated)
- Times are in Bangladesh timezone

## 🏗️ Architecture

```
railway-electricity-bot/
├── Dockerfile              # Docker container config
├── railway.json            # Railway deployment config
├── main.py                 # Entry point with health checks
├── scheduled_scraper.py    # Scheduling coordinator
├── scraper.py              # Web scraping logic
├── telegram_bot.py         # Telegram integration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 📊 Monitored Meters

| Meter Number | Nickname | Description |
|-------------|----------|-------------|
| 37226784 | Ayon | Primary meter |
| 37202772 | Arif | Secondary meter |
| 37195501 | Payel | Third meter |
| 37226785 | Piyal | Fourth meter |
| 37202771 | Solo | Fifth meter |

## 🔧 Health Monitoring

The bot provides several endpoints for monitoring:

- `GET /` - Status dashboard
- `GET /health` - Health check (for Railway)
- `GET /status` - Detailed status information

## 🧪 Testing

### Test Mode
Set `TEST_RUN=true` to run a single scraping cycle and exit:

```bash
# In Railway environment variables
TEST_RUN=true
```

### Local Testing (Optional)
```bash
# Clone the repository
git clone <your-repo-url>
cd railway-electricity-bot

# Install dependencies
pip install -r requirements.txt

# Set environment variables
export TELEGRAM_BOT_TOKEN="your_token"
export TELEGRAM_CHAT_ID="your_chat_id"
export TEST_RUN="true"

# Run test
python main.py
```

## 🚂 Railway Deployment Details

### Why Railway?
- ✅ **24/7 Operation**: Unlike Replit which auto-sleeps
- ✅ **Hobby Plan**: $5/month for unlimited runtime
- ✅ **Docker Support**: Reliable Chrome/Selenium environment
- ✅ **Auto-Scaling**: Handles traffic spikes
- ✅ **Built-in Monitoring**: Health checks and logs

### Docker Configuration
- **Base Image**: Python 3.12 slim
- **Chrome Version**: Latest stable
- **ChromeDriver**: Auto-downloaded to match Chrome
- **Runtime**: Non-root user for security

## 📝 Logs and Monitoring

### Viewing Logs
1. Go to Railway dashboard
2. Click on your project
3. Navigate to "Deployments" tab
4. Click on latest deployment
5. View real-time logs

### Log Types
- 📅 **Scheduled runs**: Daily scraping execution
- 🔋 **Meter data**: Balance information and warnings
- ❌ **Errors**: Failed scraping attempts or API errors
- 💚 **Health checks**: Service status confirmations

## 🔒 Security Features

- 🔐 **Environment Variables**: No hardcoded credentials
- 🏃 **Non-root User**: Container runs with limited privileges
- 🔒 **Secrets Management**: Railway handles sensitive data
- 🌐 **SSL Support**: Encrypted communication

## 🆘 Troubleshooting

### Common Issues

**1. Bot not responding**
- Check Railway deployment logs
- Verify environment variables are set
- Ensure Telegram bot token is valid

**2. Scraping failures**
- Website might have changed structure
- Check Chrome/ChromeDriver compatibility
- Verify DESCO website accessibility

**3. Schedule not working**
- Confirm `SCHEDULE_TIMES` format
- Check timezone conversion in logs
- Ensure Railway service is running

### Getting Help
1. Check Railway deployment logs first
2. Verify all environment variables
3. Test with `TEST_RUN=true` first
4. Review health check endpoint (`/health`)

## 🔄 Updates and Maintenance

### Updating the Bot
1. Push changes to GitHub repository
2. Railway will auto-deploy new version
3. Zero-downtime deployment

### Monitoring
- Railway provides built-in metrics
- Health endpoints for external monitoring
- Telegram notifications for issues

## 💰 Cost Estimate

**Railway Hobby Plan**: $5/month
- Includes 500 hours of usage (24/7 operation)
- $0.000463 per GB-hour after limit
- Estimated monthly cost: ~$5-7 total

## 🎉 Success Indicators

When working correctly, you should see:
- ✅ Daily Telegram messages (if balances are low)
- ✅ Bot startup notification when deployed
- ✅ Health check endpoint responding at `/health`
- ✅ Logs showing successful meter readings

---

## 📞 Support

For issues specific to this Railway version:
1. Check Railway deployment logs
2. Verify environment variables
3. Test health endpoints
4. Review Telegram bot configuration

**Previous Replit Version**: This is a Railway-optimized version. The original Replit version had auto-sleep issues that required keep-alive mechanisms - this version eliminates those problems with true 24/7 operation.