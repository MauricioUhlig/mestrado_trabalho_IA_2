# TP2-IA - Solução de Problemas de Otimização

Arquivo original disponível em:  
[Link para o Colab](https://colab.research.google.com/drive/1-Q5oDvx7OWg_FORKEblDRjL00H_7nenJ)

---

# Inteligência Artificial  
## EP2: Estudo Comparativo de Algoritmos de Otimização  
### PPCOMP - IFES - Campus Serra  

**Professor:** Sérgio Nery Simões  
**Aluno:** Mauricio Jastrow Uhlig  
**Turma:** 2024/2  

---

### Descrição do Trabalho  

**Contexto:**  
Este projeto de programação consiste em comparar o desempenho dos algoritmos de otimização aplicados a diferentes problemas. Os resultados do projeto serão:  
1. O **código desenvolvido** para cada problema.  
2. Um **breve relatório** apresentando e discutindo os resultados comparativos.  

Os algoritmos a serem comparados incluem:  
- **[HC-C] - Hill-Climbing (clássico);**  
- **[HC-R] - Hill-Climbing with Restart;**  
- **[SA] - Simulated Annealing;**  
- **[GA] - Genetic Algorithm.**  

**Desenvolvimento:**  
Os algoritmos devem ser aplicados na busca pela solução ótima de dois problemas definidos a seguir. Cada problema inclui:  
- Definição de uma **função objetivo**;  
- **Funções específicas** para geração de vizinhos;  
- No caso do GA, funções para **mutação** e **crossover**;  
- Parâmetros que devem ser usados pelos métodos.  

Os algoritmos de otimização devem ser executados pelo menos **10 vezes**, para permitir a análise de **variabilidade** dos resultados no relatório.

### Problemas  

1. **Problema 1: *Travelling Salesman Problem* (TSP)**  
   Resolver o problema do caixeiro-viajante, otimizando o trajeto.  

2. **Problema 2: Minimização da Função de Rastrigin**  
   Minimizar uma função matemática complexa frequentemente usada em benchmarks de otimização.  

### Códigos Fornecidos  

Para ajudar no desenvolvimento e prover um ambiente para testes dos algoritmos, foram fornecidos os seguintes códigos:  
- (a) Implementação do algoritmo **Hill-Climbing (clássico)** aplicado ao TSP, junto a funções para geração de **gráficos comparativos**.  
- (b) **Funções base do Algoritmo Genético (GA)**, desenvolvidas para o problema das 8-rainhas.  

A partir dos ambientes (a) e (b), os algoritmos deverão ser adaptados de acordo com as especificações de cada problema, fornecidas mais adiante. Os algoritmos principais devem ser implementados de forma **modular**, com alterações específicas concentradas em funções dedicadas a cada problema.  

---

**Observações importantes:**  
- **É proibido** utilizar bibliotecas que implementem diretamente os algoritmos de otimização.  
- **É permitido** o uso de bibliotecas auxiliares para manipulação de **estruturas de dados**.  

A implementação desses algoritmos e sua aplicação em problemas reais são úteis em entrevistas técnicas para empresas de grande porte, representando um investimento valioso na sua carreira profissional.

---
# Execução do projeto 
Para executar, basta realizar o `clone` do repositório e executar o arquivo `main.py`. 

A execução por padrão irá gerar `DataFrames` com os **custos**, quantidade de acessos na **função objetivo** e os **tempos de execução**. Além de **retornar a solução encontrada**
> Caso seja necessário alterar algum parâmetro, basta editar o arquivo `main.py`