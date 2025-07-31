# Verificador de Vogal e Consoante

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![Status](https://img.shields.io/badge/Status-Concluído-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

Programa simples em Python que identifica se uma letra digitada pelo usuário é uma vogal ou consoante, com validação robusta de entrada.

## Descrição do Projeto

Este projeto foi desenvolvido como exercício de **programação básica** e **validação de entrada** em Python. O programa demonstra conceitos fundamentais como estruturas condicionais, loops, validação de dados e modularização de código.

### Problema Resolvido
- **Cenário:** Necessidade de classificar letras do alfabeto
- **Solução:** Sistema de validação que aceita apenas letras únicas
- **Resultado:** Classificação precisa entre vogais e consoantes

## Funcionalidades

- **Validação de Entrada:** Aceita apenas letras do alfabeto
- **Verificação de Tamanho:** Impede entrada de múltiplos caracteres
- **Classificação Automática:** Identifica vogais (a, e, i, o, u) e consoantes
- **Case Insensitive:** Funciona com letras maiúsculas e minúsculas
- **Loop de Correção:** Solicita nova entrada até receber dados válidos
- **Feedback Claro:** Mensagens informativas sobre o resultado

## Tecnologias

- **Python 3.x**
- **Métodos de String:** `.isalpha()`, `.lower()`
- **Estruturas de Controle:** `while`, `if/else`
- **Estruturas de Dados:** Tuplas para armazenar vogais

## Como Executar

### Pré-requisitos
- Python 3.6 ou superior instalado

### Passos
1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/verificador-vogal-consoante.git
   cd verificador-vogal-consoante
   ```

2. **Execute o programa:**
   ```bash
   python verificador.py
   ```

3. **Interaja com o programa:**
   - Digite uma letra quando solicitado
   - Receba o resultado da classificação

## Preview do Sistema

```
Insira uma letra para verificar se é consoante ou vogal: 123

O caracter '123' não é uma letra! Insira uma letra!

Insira uma letra para verificar se é consoante ou vogal: a

O caracter 'a' é uma letra!

'a' é uma vogal
```

## Estrutura do Código

### Arquivo Principal
- **`verificador.py`** - Sistema completo de verificação

### Principais Funções
```python
def ler_caracter()          # Captura entrada do usuário
def verificar_letra()       # Valida se é letra única
def exibir_erro()           # Fornece feedback sobre entrada  
def tipo_letra()            # Classifica vogal ou consoante
def main()                  # Fluxo principal do programa
```

## Conceitos Aplicados

### Validação de Dados
- **Método `.isalpha()`:** Verificação se caractere é letra
- **Função `len()`:** Validação de tamanho da entrada
- **Tratamento de Casos:** Distinção entre entradas válidas e inválidas

### Estruturas de Controle
- **Loop While:** Repetição até entrada válida
- **Condicionais:** Classificação lógica de caracteres
- **Operadores de Comparação:** Verificação de pertencimento

### Boas Práticas
- **Modularização:** Separação de responsabilidades em funções
- **Case Insensitive:** Conversão para minúsculas antes da comparação
- **Feedback ao Usuário:** Mensagens claras sobre operações

## Especificações Técnicas

- **Entrada:** Um único caractere alfabético
- **Saída:** Classificação como vogal ou consoante
- **Vogais Reconhecidas:** a, e, i, o, u (maiúsculas e minúsculas)
- **Validações:** Apenas letras, tamanho único
- **Compatibilidade:** Multiplataforma (Windows, Linux, macOS)

## Exemplo de Uso

| Entrada | Resultado |
|---------|-----------|
| `a` | 'a' é uma vogal |
| `B` | 'B' é uma consoante |
| `123` | Erro: não é uma letra |
| `abc` | Erro: mais de um caractere |

## Aprendizados

Este projeto consolidou conhecimentos em:
- **Validação robusta de entrada do usuário**
- **Estruturas condicionais e loops**
- **Métodos nativos de strings em Python**
- **Modularização e organização de código**
- **Tratamento de diferentes tipos de entrada**

## Melhorias Futuras

- [ ] Suporte para caracteres acentuados (á, ê, í, ô, ü)
- [ ] Interface gráfica com Tkinter
- [ ] Modo batch para processar múltiplas letras
- [ ] Estatísticas de uso (contador de vogais/consoantes)
- [ ] Suporte para outros idiomas

## Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Contato

**Natan Mauricio Santos**
📧 Email: natanmauriciosantos@hotmail.com
💼 LinkedIn: linkedin.com/in/natan-mauricio-santos
🐙 GitHub: github.com/NatanMauricio1995

---

Se este projeto te ajudou, deixe uma estrela!

*Desenvolvido como exercício de programação básica em Python*
