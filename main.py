#!/usr/bin/env python3
"""
Railway Electricity Meter Bot - Main Entry Point
Monitors multiple DESCO prepaid electricity meters and sends Telegram updates.
Optimized for Railway deployment with 24/7 operation.
"""

import os
import sys
import logging
from threading import Thread
from flask import Flask
from scheduled_scraper import ScheduledMeterScraper

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('scraper.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

# Create Flask app for health checks (required by Railway)
app = Flask(__name__)

@app.route('/')
def home():
    """Home page showing bot status"""
    schedule_times = os.environ.get('SCHEDULE_TIMES', '08:00')
    return f"""
    <h1>🔋 Electricity Meter Bot - Railway</h1>
    <p><strong>Status:</strong> Running 24/7 on Railway</p>
    <p><strong>Schedule:</strong> Daily at {schedule_times} (Bangladesh Time)</p>
    <p><strong>Meters:</strong> Ayon, Arif, Payel, Piyal, Solo</p>
    <p><strong>Features:</strong> Smart recharge detection enabled</p>
    <p><strong>Platform:</strong> Railway Hobby Plan</p>
    <p>Check console logs for detailed activity</p>
    <hr>
    <p><small>Bot will automatically restart if it crashes. No manual intervention needed.</small></p>
    """

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return {
        "status": "healthy",
        "service": "electricity-meter-bot",
        "platform": "railway",
        "features": ["telegram-notifications", "smart-recharge-detection", "multi-meter-monitoring"]
    }

@app.route('/status')
def status():
    """Status endpoint with more details"""
    return {
        "service": "Railway Electricity Meter Bot",
        "version": "2.0-railway",
        "meters_monitored": 5,
        "schedule_times": os.environ.get('SCHEDULE_TIMES', '08:00'),
        "test_mode": os.environ.get('TEST_RUN', 'false').lower() == 'true',
        "platform": "Railway Hobby Plan"
    }

def run_flask_app():
    """Run Flask app in a separate thread"""
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)

def main():
    """Main function to start the bot"""
    logging.info("="*60)
    logging.info("🚀 STARTING RAILWAY ELECTRICITY METER BOT")
    logging.info("="*60)
    logging.info("Platform: Railway Hobby Plan")
    logging.info("Meters: 5 (Ayon, Arif, Payel, Piyal, Solo)")
    logging.info("Features: Smart recharge detection, 24/7 monitoring")
    
    # Start Flask server in background thread for health checks
    flask_thread = Thread(target=run_flask_app, daemon=True)
    flask_thread.start()
    logging.info(f"✅ Health check server started on port {os.environ.get('PORT', 8080)}")
    
    # Create scheduler instance
    scheduler = ScheduledMeterScraper()
    
    # Check if running in test mode
    test_run = os.getenv('TEST_RUN', 'false').lower() == 'true'
    
    if test_run:
        logging.info("🧪 TEST MODE: Running single scraping cycle...")
        try:
            scheduler.run_daily_scraping()
            logging.info("✅ Test run completed successfully!")
        except Exception as e:
            logging.error(f"❌ Test run failed: {e}")
            sys.exit(1)
    else:
        logging.info("📅 PRODUCTION MODE: Starting scheduled monitoring...")
        logging.info("The bot will run 24/7 and automatically restart if it crashes")
        try:
            scheduler.start_scheduler()
        except Exception as e:
            logging.error(f"❌ Scheduler failed: {e}")
            # Railway will automatically restart the service
            sys.exit(1)

if __name__ == "__main__":
    main()