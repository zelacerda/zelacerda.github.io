function share(text) {
    if (navigator.share) {
        navigator.share({title:text, text:text})
            .then(() => console.log('Successful share'))
            .catch((error) => console.log('Error sharing:', error));
        return;
    } else {
        navigator.clipboard.writeText(text)
            .then(() => alert('Resultado copiado para a área de transferência.'))
            .catch((error) => console.error('Clipboard error:', error));
        return;
    }
}