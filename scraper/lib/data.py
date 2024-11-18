import yfinance as yf
import json



def get_name_from_ticker(input_data_file, output_data_file=None):
    with open(input_data_file, 'r') as f:
        data = json.load(f)


    d = {}

    for ticker in data:
        stock = yf.Ticker(ticker)
        
        company_info = stock.info
        company_name = company_info.get('longName', 'Unknown Company')
        
        print(f"Ticker: {ticker}, Company: {company_name}")
        
        # Store in dictionary
        d[ticker] = company_name

    if output_data_file is None:
        output_data_file = input_data_file  
    with open(output_data_file, 'w') as f:
        json.dump(d, f, indent=4)

    print("Updated data saved to biotech.json.")

# s=get_name_from_ticker('/Users/simarmalhotra/Desktop/projects/pharma/data/biotech.json')



p=yf.Sector('pharmaceutical-retailers')
print(p.name )

# def get_ticker_from_name(input_data_file, output_data_file=None):

#     with open(input_data_file, 'r') as f:
#         data = json.load(f)

#     d = {}

#     for company_name in data:
        
#         try:
            
#             stock = yf.Ticker(company_name)
#             company_info = stock.info
#             ticker = company_info.get('symbol', None)  #

#             if ticker:
#                 print(f"Company: {company_name}, Ticker: {ticker}")
#                 d[company_name] = ticker
#             else:
#                 print(f"Could not find ticker for {company_name}")

#         except Exception as e:
#             print(f"Error fetching data for {company_name}: {e}")
    
    
#     if output_data_file is None:
#         output_data_file = input_data_file  

#     with open(output_data_file, 'w') as f:
#         json.dump(d, f, indent=4)

#     print(f"Updated data saved to {output_data_file}")


# s = get_ticker_from_name('/Users/simarmalhotra/Desktop/projects/pharma/data/companies.json')


