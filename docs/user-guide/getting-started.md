-----------------------
Setup and Installation
------------------------

# Clone the repository
git clone https://github.com/yourusername/real-estate-metals-analysis.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
docker-compose up -d postgres

# Run migrations
alembic upgrade head