# #!/usr/bin/env python3

# from sqlalchemy import create_engine

# from models import Company, Dev

# if __name__ == '__main__':
#     engine = create_engine('sqlite:///freebies.db')
#     import ipdb; ipdb.set_trace()

from seed import Session, Dev, Company, Freebie

session = Session()

# Fetch and print all companies
print("\n🧱 Companies:")
for company in session.query(Company).all():
    print(company)

# Fetch and print all developers
print("\n👨‍💻 Developers:")
for dev in session.query(Dev).all():
    print(dev)

# Fetch and print all freebies
print("\n🎁 Freebies:")
for freebie in session.query(Freebie).all():
    print(freebie)

# Example: Check what companies a developer has received freebies from
print("\n🔍 Developer Freebie Summary:")
for dev in session.query(Dev).all():
    print(f"{dev.name} received freebies from: {[c.name for c in dev.companies]}")

# Optional: Oldest company
oldest = Company.oldest_company()
print(f"\n🏛️ Oldest Company: {oldest.name} (Founded {oldest.founding_year})")
