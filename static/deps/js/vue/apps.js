
// var app = new Vue({
//     delimiters: ['[[', ']]'],
//     el: '#app',
//     data: {
//         count: 0,
//     },
//     mounted() {
//         console.log(this.message)
//     },
//     methods: {
//         click_minus() {
//             this.count--;
//         },
//         click_plus() {
//             this.count++;
//         },
// async cart_add(product_id) {
//     console.log(product_id)
//     let url = document.getElementById('cart_add').href
//     let csrf_token = grabToken()
//     // let csrf_token = document.getElementsByName('csrfmiddlewaretoken')[0].defaultValue
//     console.log(url)
//     console.log(csrf_token)

//     let formdata = new FormData()

//     formdata.append("product_id", product_id)
//     formdata.append("csrfmiddlewaretoken", csrf_token)

//     axios({
//         method: 'post',
//         url: url,
//         data: formdata
//     }).then(function (response) {
//         console.log(response)
//     });
// }
//     }
// })