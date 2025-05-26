#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Company, Dev, Freebie

engine = create_engine('sqlite:///freebies.db')

# Create all tables (only needed if not using Alembic to handle schema)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Clear old data
session.query(Freebie).delete()
session.query(Company).delete()
session.query(Dev).delete()
session.commit()

# Seed companies
company1 = Company(name="TechCorp", founding_year=2000)
company2 = Company(name="InnoSoft", founding_year=1998)

# Seed devs
dev1 = Dev(name="Alice")
dev2 = Dev(name="Bob")
dev3 = Dev(name="Charlie")

# Seed freebies
freebie1 = Freebie(item_name="T-Shirt", value=25, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Mug", value=10, dev=dev1, company=company2)
freebie3 = Freebie(item_name="Stickers", value=5, dev=dev2, company=company2)

# Add and commit
session.add_all([company1, company2, dev1, dev2, dev3, freebie1, freebie2, freebie3])
session.commit()

print("🌱 Seeding complete!")
