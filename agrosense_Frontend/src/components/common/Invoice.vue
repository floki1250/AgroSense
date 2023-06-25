<template>
  <div>
    <ClientOnly> <iframe id="pdf" width="100%" height="500px" /></ClientOnly>
  </div>
</template>

<script setup>
import { useNuxtApp } from '#app';

const { $pdf } = useNuxtApp()

$pdf.new({
  plugins: [
    {

      page: [
        // simple counter footer
        ({ Text }, context, current, total) => {
          // render in every page
          Text(`${current}/${total}`, { fontSize: 12 }, {
            x: context.width / 2,
            y: context.height - context.margins.bottom
          })
        },
        // simple header
        ({ Text }, context, current, total) => {
          // render in every page
          Text('Purchase Invoice', { fontSize: 24 }, {
            x: context.width / 2.2,
            y: context.margins.top - 20
          })
          // render in every page

        }
      ]
    }
  ]
})

$pdf.add([
  { lineBreak: {} }, // line break
  { raw: '_________________________________________', text: { fontSize: 22 } },
  { lineBreak: {} },
  { raw: 'Ship Date : ', text: { fontSize: 12 } },
  { lineBreak: {} }, // line break
  { raw: 'From : AgroSense Company', text: { fontSize: 12 } },
  { lineBreak: {} }, // line break
  { raw: 'To : ', text: { fontSize: 12 } },
  { raw: '_________________________________________', text: { fontSize: 22 } },
  { lineBreak: {} }, // line break
  { raw: '_________________________________________', text: { fontSize: 22 } },
  // external image
  {
    table: { // table. Check pdfkit-table package for more explanations
      body: {
        headers: ["Item ID", "Quantity", "Unit Price", "Unit Of Measure", "Cost"],
        rows: [
          ["1", 100, 1.5, "Kg", 500],
          ["1", 100, 1.5, "Kg", 500],
          ["1", 100, 1.5, "Kg", 500],
          ["1", 100, 1.5, "Kg", 500],
          ["Total", "", "", "", 500],
        ],
      },
      options: {}
    },

  },

])


$pdf.run().then(blob => {
  const iframe = document.querySelector('#pdf')

  iframe.src = blob
}).catch((err) => {
  console.error(err)
})
</script>
