# Mini Seminário — Tailwind CSS

Trabalho da disciplina **Desenvolvimento Web** (Prof. Iuri Santos · Unilasalle 2026/1).
Framework: **Tailwind CSS** (utility-first), versão de referência 4.2.x.

**Dupla:** _[preencher nomes]_

## Conteúdo do repositório

| Arquivo | O que é | Critério de avaliação |
|---|---|---|
| `enunciado.pdf` | Enunciado original da atividade | — |
| `artigo-tecnico.md` | Mini artigo técnico (histórico, filosofia, box model/flexbox/responsividade, vantagens×CSS3, casos de uso, instalação CDN+NPM, referências) | Artigo Técnico (10%) + base p/ Domínio Técnico (40%) |
| `aula-simples/index.html` | **Componente que se replica ao vivo em aula** — grid responsivo de cards, ~25 linhas | Domínio Técnico (40%) + Qualidade do Código (30%) |
| `aula-simples/cola.md` | Roteiro de digitação + as 4 frases pra falar durante o live coding | apoio ao Pitch |
| `componente/index.html` | Versão elaborada (navbar + cards + form) — backup / prova de domínio | Domínio Técnico (40%) |
| `com-framework/index.html` | Mesmo card grid, mas componentizado em React (CDN, sem build) — mostra como o framework tira a "poluição" | Domínio Técnico (40%) |
| `com-framework/por-que.md` | Explicação antes×depois: papel do framework + frase de efeito p/ o pitch | apoio ao Pitch |
| `pitch.md` | Roteiro do pitch cronometrado (3–5 min), divisão da dupla, munição p/ perguntas | Comunicação/Pitch (20%) |

## Como rodar

Abrir qualquer `index.html` direto no navegador — usa Tailwind v4 via CDN, **sem build**.
Redimensionar a janela para ver o grid responsivo (1 → 3 colunas no breakpoint `md:` = 768px).

```bash
xdg-open aula-simples/index.html
```

## Checklist de entrega

- [ ] Nomes da dupla preenchidos (`README.md`, `artigo-tecnico.md`, `pitch.md`)
- [ ] Artigo exportado para **PDF** (entregável exige PDF)
- [ ] Pitch ensaiado com cronômetro (alvo 4:30, teto 5:00)
- [ ] Live coding ensaiado digitando do zero olhando só o esqueleto da `cola.md`
- [ ] Plano B se a internet cair na sala (CDN precisa de rede) — print/gravação salvos
- [ ] Uso de IA citado conforme política da disciplina

## Nota de integridade acadêmica

Material produzido com assistência de IA como base de pesquisa e estruturação.
A dupla deve ler, entender, validar tecnicamente e citar o uso de IA conforme a
política da disciplina antes de submeter — o domínio técnico cobrado no pitch
(40%) só se sustenta se o conteúdo for genuinamente absorvido.
