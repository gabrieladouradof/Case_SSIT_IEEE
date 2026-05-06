# 👁️ Projeto Íris - Dashboard de Triagem Preditiva

Este repositório contém o protótipo funcional desenvolvido para o **Case Prático da IEEE SSIT UnB (2026)**. [cite_start]O foco do projeto é a **Otimização Estratégica e Preventiva** no combate ao trabalho análogo à escravidão em contextos urbanos[cite: 4, 38].

---

## ⚠️ Aviso: Protótipo de Conceito (PoC)
[cite_start]Este software é um **protótipo em estágio embrionário**[cite: 63]. [cite_start]Ele foi desenvolvido para demonstrar a viabilidade técnica de utilizar inteligência de dados para suporte à fiscalização, não devendo ser utilizado como ferramenta final de diagnóstico sem a devida validação de especialistas humanos (*Human-in-the-loop*)[cite: 66].

---

## 🎯 Sobre o Projeto
[cite_start]O Projeto Íris busca identificar, através de dados públicos, anúncios de vagas fraudulentas que servem como iscas para o aliciamento de trabalhadores vulneráveis no Distrito Federal e Entorno[cite: 35, 54]. 

Diferente de soluções intrusivas, esta ferramenta foca na **Prevenção Primária**:
1. [cite_start]**Cruzamento de Metadados:** Verifica se o anunciante consta na "Lista Suja" do MTE (Cadastro de Empregadores)[cite: 71, 74].
2. [cite_start]**Análise Semântica:** Identifica gatilhos textuais de risco (ex: ganhos irreais, urgência extrema)[cite: 61].
3. [cite_start]**Apoio Educativo:** Os resultados alimentam campanhas físicas de conscientização lideradas pela IEEE EdSoc[cite: 60, 86].

---

## 🚀 Como Testar o Protótipo
Você pode acessar o dashboard online aqui: **[https://triagempreditivairis.streamlit.app/]**

Para validar as funcionalidades do algoritmo, siga os passos abaixo:

### 1. Teste de Cruzamento (Lista Suja 2026)
* **Ação:** No campo "CNPJ", insira o seguinte número simulado: `12.345.678/0001-90`.
* [cite_start]**Resultado Esperado:** O sistema emitirá um **Alerta Crítico (Vermelho)** informando que a empresa consta no cadastro de infratores atualizado em abril de 2026[cite: 74, 90].

### 2. Teste de Gatilhos de Risco (NLP)
* **Ação:** No campo de texto da vaga, cole um anúncio que contenha termos como: *"Viagem imediata com tudo pago"*, *"Ganhos altos sem experiência"* ou *"Necessário entregar documentos originais"*.
* **Resultado Esperado:** O sistema exibirá um **Aviso de Alerta (Amarelo)** destacando os sinais de aliciamento digital, em conformidade com o material educativo da SSIT.

---

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python
* **Interface:** Streamlit
* [cite_start]**Lógica Preditiva:** Conceitos de LightGBM e Processamento de Linguagem Natural (NLP)[cite: 75].
* [cite_start]**Base de Dados:** Cadastro de Empregadores do MTE (Abril/2026)[cite: 90].

---

## 👥 Integrantes - Grupo 1
* **Gabriela:** Desenvolvimento Tecnológico
* **Lucas Silva:** Pesquisa e Extensão
* **Fernanda:** Comunicação e Marketing

---
[cite_start]*Este projeto foi desenvolvido respeitando as fronteiras metodológicas e éticas do documento fundacional do Projeto Íris, priorizando a privacidade e o impacto social positivo[cite: 58, 85].*
