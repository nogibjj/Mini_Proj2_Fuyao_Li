from main import generate_dataframe, generate_describe, \
    generate_average_temperature, generate_heatmap, generate_markdown


# Specify the file path and the sheet name
file_path = 'Durham-Observatory-monthly-mean-temperature.xlsx'
sheet_name = 'Durham monthly Tmean'


def test_generate_dataframe():
    df = generate_dataframe(file_path, sheet_name)
    assert df.iloc[0, 0] == 1795


def test_generate_describe():
    df = generate_dataframe(file_path, sheet_name)
    stats_df = generate_describe(df)
    assert round(stats_df.iloc[0, 0], 2) == 2.89


def test_generate_average_temperature():
    df = generate_dataframe(file_path, sheet_name)
    generate_average_temperature(df)


def test_generate_heatmap():
    df = generate_dataframe(file_path, sheet_name)
    generate_heatmap(df)


def test_generate_markdown():
    df = generate_dataframe(file_path, sheet_name)
    stats_df = generate_describe(df)
    generate_markdown(stats_df)


if __name__ == "__main__":
    test_generate_dataframe()
    test_generate_describe()
    test_generate_average_temperature()
    test_generate_heatmap()
    test_generate_markdown()
