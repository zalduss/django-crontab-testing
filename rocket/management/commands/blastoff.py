from django.core.management.base import BaseCommand # type: ignore
import traceback
import logging
import os
import time
from pathlib import Path


class Command(BaseCommand):
    help = 'Rocket countdown and blastoff simulation'
    
    def handle(self, *args, **kwargs):
        # Setup logging
        log_dir = Path('logs')
        log_dir.mkdir(exist_ok=True)
        
        log_file = "/Users/zald/files/projects/cloud-learning/cloud-django-cronjob/backend/logs/blastoff.log"
        
        logging.basicConfig(
            filename=str(log_file),
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        
        logger = logging.getLogger('blastoff')
        
        try:
            # Start countdown from 5 seconds
            for i in range(5, -1, -1):
                message = f"T-minus {i} seconds..."
                self.stdout.write(message)
                logger.info(message)
                time.sleep(1)
            
            # Blast off!
            blastoff_message = "BLAST OFF! 🚀"
            self.stdout.write(self.style.SUCCESS(blastoff_message))
            logger.info(blastoff_message)
            
        except Exception as e:
            error_msg = f"An error occurred: {str(e)}"
            traceback_msg = f"Traceback:\n{traceback.format_exc()}"
            
            print(error_msg)
            print(traceback_msg)
            
            logger.error(error_msg)
            logger.error(traceback_msg)