$("body").on("click", "#btnExport", function () {
    html2canvas($('#dataTable')[0], {
        onrendered: function (canvas) {
            var data = canvas.toDataURL();
            var docDefinition = {
                content: [{
                    image: data,
                    width: 520
                }]
            };
            pdfMake.createPdf(docDefinition).download("Foods-detail.pdf");
        }
    });
});