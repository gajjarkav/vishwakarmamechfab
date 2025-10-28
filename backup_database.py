#!/usr/bin/env python
'''
SQLite Database Backup Script for VMF Project
Run this regularly to backup your database
'''

import os
import shutil
import sqlite3
from datetime import datetime
from pathlib import Path

def backup_database():
    db_path = 'db.sqlite3'
    if not os.path.exists(db_path):
        print("❌ Database file not found!")
        return False
    
    # Create backups directory
    backup_dir = Path('backups')
    backup_dir.mkdir(exist_ok=True)
    
    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = backup_dir / f'db_backup_{timestamp}.sqlite3'
    
    try:
        # Method 1: Simple file copy (fastest)
        shutil.copy2(db_path, backup_file)
        
        # Method 2: SQLite backup (more reliable for active databases)
        # Uncomment if you prefer this method:
        # src = sqlite3.connect(db_path)
        # dst = sqlite3.connect(backup_file)
        # src.backup(dst)
        # src.close()
        # dst.close()
        
        file_size = os.path.getsize(backup_file) / 1024  # KB
        print(f"✅ Database backed up successfully!")
        print(f"   File: {backup_file}")
        print(f"   Size: {file_size:.1f} KB")
        
        # Clean up old backups (keep last 10)
        backups = sorted(backup_dir.glob('db_backup_*.sqlite3'))
        if len(backups) > 10:
            for old_backup in backups[:-10]:
                old_backup.unlink()
                print(f"🗑️  Removed old backup: {old_backup.name}")
        
        return True
        
    except Exception as e:
        print(f"❌ Backup failed: {e}")
        return False

if __name__ == "__main__":
    print("💾 SQLite Backup Tool for Vishwakarma Mechfab")
    print("=" * 50)
    backup_database()
