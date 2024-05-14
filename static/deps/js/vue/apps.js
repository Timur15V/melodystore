var app = new Vue({
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        message: "Hello, Vue!",
    },
    mounted() {
        console.log(this.message)
    },
    methods: {
        clickCart() {
            console.log(this.message);
        }
    }
})