#!/bin/bash
# build_files.sh

# Install dependencies
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate

# Make sure the script exits successfully
echo "Build completed successfully"
