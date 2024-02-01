import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

#função que inicia o programa
def run():
    st.set_page_config(
        page_title="Paulistao"
    )

    st.title("Análise sobre o Corinthians no Paulistão")

    st.sidebar.success("Selecione o ano")

    st.markdown(
        """
        Com 30 títulos conquistados, o Corinthians é o maior vencedor do Campeonato Paulista. Sua rica história no torneio é marcada por momentos memoráveis, como o tricampeonato consecutivo entre 1922 e 1924, a hegemonia na década de 30 com cinco títulos em seis anos, e o bicampeonato histórico de 2017 e 2018.
        """
    )
    st.subheader("Analisando os Últimos 3 Anos:")
    st.markdown(
        """
        2020: Um ano de frustração. O Corinthians caiu nas quartas de final para o Mirassol, após um empate em casa e uma derrota fora.
        
        2021: A redenção! O Timão dominou o campeonato, com a melhor campanha da fase de grupos e vitórias emocionantes nas fases finais. Na final, superou o rival Palmeiras nos pênaltis, após empate no tempo normal e na prorrogação.
        
        2022: Uma campanha irregular resultou na eliminação nas semifinais para o São Paulo. Apesar de um bom início, o time não conseguiu manter a regularidade e caiu diante do rival.
       """
    )
    
    st.subheader("Mergulhando nos Dados:")
    st.markdown(
        """
        2020: 13 jogos, 6 vitórias, 3 empates e 4 derrotas. 20 gols marcados e 14 sofridos. 

        2021: 16 jogos, 9 vitórias, 5 empates e 2 derrotas. 27 gols marcados e 11 sofridos.

        2022: 15 jogos, 7 vitórias, 4 empates e 4 derrotas. 22 gols marcados e 15 sofridos.
        """
    )
    st.subheader("O que esperar para 2024:")
    st.markdown(
        """
        Elenco em reformulação: O Corinthians perdeu jogadores importantes como Renato Augusto, Gil, Fabio Santos, Giuliano e ainda busca reforços para o setor defensivo e ofensivo.
        
        técnico: Mano menezes segue no comando da equipe, mas ainda precisa provar que esta passagem pode ser vitoriosa, mas que não será nada fácil.
        
        Expectativa incerta: A torcida espera um ano de conquistas, mas o time ainda precisa se encaixar e mostrar regularidade.
       
        Nova Diretoria: A nova direção assumiu em janeiro com muitas promessas de mudanças o que causa eperança na Fiel Torcida, com um patrocinio Milhonário assinado para o master, ainda contem incertezas a respeito das dividas do clube e a situação da reformulação e reforços do elenco.
        
    
        Explore a página para:

        Visualizar dashboards interativos com estatísticas detalhadas dos últimos 3 anos.
        Analisar o desempenho do time em diferentes aspectos, como ataque, defesa e posse de bola.
        Identificar pontos fortes e fracos da equipe.
        Comparar o desempenho do Corinthians com seus principais rivais.
        Descobrir insights e tendências para o Campeonato Paulista de 2023.

        Junte-se à Fiel e vibre com o Corinthians!

        #VaiCorinthians
    """
    )


if __name__ == "__main__":
    run()
