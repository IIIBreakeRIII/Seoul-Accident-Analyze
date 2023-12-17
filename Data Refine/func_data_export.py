import pandas as pd

def data_merge_sort(data, export_name):

    # Make new Dataframe by condition
    df_damage = data[data['피해운전자 차종'].isin(["보행자", "이륜", "원동기", "이륜", "개인형이동수단(PM)"])]
    df_violent = data[data['가해운전자 차종'].isin(["보행자", "이륜", "원동기", "이륜", "개인형이동수단(PM)"])]

    # Merge to Dataframe and sort by 사고번호
    df_OUTER_JOIN_all = pd.merge(df_damage, df_violent, how='outer')
    df_all_SORT_VALUES = df_OUTER_JOIN_all.sort_values(by='사고번호', ascending=True)

    # Check merge and save new csv by condition and sort by num
    print(export_name, "= MERGE AND SORT DONE")
    directory = "./Data/TAAS/after_merge_damage_violent/"
    df_all_SORT_VALUES.to_csv(path_or_buf=directory + export_name + ".csv")