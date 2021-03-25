import pandas as pd

def main():
    dataframe = pd.read_csv('UserInfo.csv')
    print(dataframe)

    print(dataframe['NID'][2])




if __name__=='__main__':
    main()