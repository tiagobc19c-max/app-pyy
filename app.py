import streamlit as st

def calcular_gasto_uber():
    st.title("🚗 Cálculo de Combustível - Uber")
    st.write("Divisão de custos baseada na quilometragem rodada.")
    
    # Informação fixa do rendimento do veículo
    CONSUMO_KM_L = 8.0  # 8 km por litro no álcool
    
    # Entrada de dados na tela
    preco_litro = st.number_input("Preço do litro do combustível (R$):", min_value=0.0, value=5.00, step=0.05)
    
    st.markdown("---")
    st.subheader("Mateus")
    km_ini_1 = st.number_input("KM inicial (Mateus):", min_value=0.0, value=0.0, step=1.0)
    km_fim_1 = st.number_input("KM final (Mateus):", min_value=0.0, value=0.0, step=1.0)
    
    st.markdown("---")
    st.subheader("Tiago")
    km_ini_2 = st.number_input("KM inicial (Tiago):", min_value=0.0, value=0.0, step=1.0)
    km_fim_2 = st.number_input("KM final (Tiago):", min_value=0.0, value=0.0, step=1.0)
    
    # Botão para calcular
    if st.button("Calcular Fechamento"):
        km_rodados_1 = km_fim_1 - km_ini_1
        km_rodados_2 = km_fim_2 - km_ini_2
        
        if km_rodados_1 < 0 or km_rodados_2 < 0:
            st.error("Erro: O KM final não pode ser menor que o KM inicial.")
            return

        # Cálculos
        litros_1 = km_rodados_1 / CONSUMO_KM_L
        litros_2 = km_rodados_2 / CONSUMO_KM_L
        
        valor_1 = litros_1 * preco_litro
        valor_2 = litros_2 * preco_litro
        
        total_km = km_rodados_1 + km_rodados_2
        total_litros = litros_1 + litros_2
        total_valor = valor_1 + valor_2
        
        # Exibição dos resultados na tela
        st.markdown("---")
        st.subheader("Resumo do Fechamento")
        
        st.info(
            f"**Mateus:** {km_rodados_1:.1f} km | {litros_1:.2f} L | **R$ {valor_1:.2f}**\n\n"
            f"**Tiago:** {km_rodados_2:.1f} km | {litros_2:.2f} L | **R$ {valor_2:.2f}**"
        )
        
        st.success(
            f"**TOTAL CONJUNTO:** {total_km:.1f} km | {total_litros:.2f} L | **R$ {total_valor:.2f}**"
        )

if __name__ == "__main__":
    calcular_gasto_uber()