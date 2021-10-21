import uuid

def generate_fund_id():
    fund_code = str(uuid.uuid4()).replace('-', '')[:6]
    return fund_code




def generate_invest_id():
    invest_code =str(uuid.uuid4()).replace('-', '')[:6]
    return invest_code