from sqlalchemy import ForeignKey, Column, Integer, String, MetaData, create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker
from base import Base
DATABASE_URL = "sqlite:///freebies.db"  # load live database / hosted db 
engine = create_engine(DATABASE_URL, echo=False)
Session = sessionmaker(bind=engine) # session blueprint 

class Company(Base):
    __tablename__ = 'companies'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    founding_year = Column(Integer())
    freebies = relationship("Freebie", back_populates="company")
    
    def __repr__(self):
        return f'<Company {self.name}>'
    
    @property
    def devs(self):
        return list({freebie.dev for freebie in self.freebies})

    def give_freebie(self, dev, item_name, value):
        session = Session()
        new_freebie = Freebie(item_name=item_name, value=value, dev=dev, company=self)
        session.add(new_freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        session = Session()
        return session.query(cls).order_by(cls.founding_year).first()

class Dev(Base):
    __tablename__ = 'devs'

    id = Column(Integer(), primary_key=True)
    name= Column(String())

    freebies = relationship("Freebie", back_populates="dev")

    def __repr__(self):
        return f'<Dev {self.name}>'
    

    @property
    def companies(self):
        return list({freebie.company for freebie in self.freebies})

    def received_one(self, item_name):
        return any(f.item_name == item_name for f in self.freebies)

    def give_away(self, dev, freebie):
        if freebie in self.freebies:
            session = Session()
            freebie.dev = dev
            session.commit()

class Freebie(Base):
    __tablename__ = "freebies"
    
    id = Column(Integer, primary_key = True)
    item_name = Column(String(15), nullable= False)
    value = Column(Integer(), nullable= False)

    # define the relationship with the company and dev tables
    dev_id = Column(Integer, ForeignKey('devs.id'))
    company_id = Column(Integer, ForeignKey('companies.id'))

    dev = relationship("Dev", back_populates="freebies")
    company = relationship("Company", back_populates="freebies")
    
    def __repr__(self):
        return f'<Freebie {self.item_name} Value {self.value} company {self.company_id} dev {self.dev_id} >'