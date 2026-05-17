# Cola de live coding — 1 card grid em Tailwind (~2 min)

Decore **o esqueleto** (não as palavras). É um card repetido 3× dentro de um grid.

## Ordem de digitação

1. **Boilerplate + CDN** (cole de uma vez, ninguém digita isso ao vivo):
   ```html
   <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
   ```
2. **`<body class="bg-slate-100 p-6">`** → *"fundo cinza, padding de 6 — isso já é box model."*
3. **Título** `<h1 class="text-2xl font-bold mb-4">Produtos</h1>`
4. **O grid responsivo** (o momento-chave):
   ```html
   <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
   ```
5. **Um card** (digita 1, copia/cola 3×):
   ```html
   <div class="bg-white p-5 rounded-xl shadow flex flex-col gap-2">
     <h2 class="font-semibold">Fone</h2>
     <p class="text-slate-500 text-sm">Bluetooth, 30h.</p>
     <button class="bg-indigo-600 text-white py-2 rounded mt-2">Comprar</button>
   </div>
   ```
6. Salva, abre no navegador, **redimensiona a janela**.

## As 4 frases que você fala enquanto digita

1. **Box model** — apontando `p-5 rounded-xl`:
   > "padding e borda arredondada sem escrever CSS — escala pronta."
2. **Flexbox** — apontando `flex flex-col gap-2`:
   > "empilho título, texto e botão na vertical com espaçamento — isso é flexbox."
3. **Grid + responsividade** — apontando `grid-cols-1 md:grid-cols-3`:
   > "1 coluna no celular, 3 a partir de 768px."
4. **O golpe** — redimensionando a janela ao vivo:
   > "reparem: **não escrevi nenhuma `@media`**. O `md:` virou media query sozinho.
   > É essa a ideia do Tailwind — responsividade declarativa, direto no HTML."

## Por que isso fecha os critérios
- **Box model (40%)** → `p-`, `rounded-`, `gap-`
- **Flexbox** → `flex flex-col`
- **Responsividade exigida** → grid nativo + `md:` (= media query automática)
- **Qualidade código (30%)** → `<h1>/<h2>/<p>/<button>` semânticos, indentado
- Total: ~25 linhas, digitável em ~2 min. Sobra tempo pro pitch.

> Internet caiu? Tenha o `index.html` já salvo aberto como plano B.
