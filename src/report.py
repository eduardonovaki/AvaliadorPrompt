import pandas as pd
import matplotlib.pyplot as plt


def gerar_tabela(resultados):
    df = pd.DataFrame(resultados)

    df.to_csv("output/resultados.csv", index=False)

    return df


def grafico_acuracia(resultados):
    df = pd.DataFrame(resultados)

    medias = df.groupby("tecnica")["acuracia"].mean()

    plt.figure(figsize=(8, 5))
    medias.plot(kind="bar")

    plt.title("Acurácia média por técnica")
    plt.xlabel("Técnica")
    plt.ylabel("Acurácia média")

    plt.savefig("output/grafico_acuracia.png")
    plt.close()