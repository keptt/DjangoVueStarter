<template>
    <div id="app">
        <div class="container" id="contact">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
            <AddProduct v-on:add-product="addProduct"/>
            <Products v-bind:products="products"    v-on:get-products="getProducts"
                                                    v-on:add-product="addProduct"
                                                    v-on:delete-product="deleteProduct"
                                                    v-on:update-product="updateProduct"
                                                    v-on:on-product-edit="onProductEdit"/>
    <!-- <router-view/> -->
        </div>
    </div>
</template>


<script>
import Products from './components/Products';
import AddProduct from './components/AddProduct.vue';
import axios from 'axios';

export default {
    name: 'app'
    , components: {
        Products
        , AddProduct
    }
    , data() {
        return {
            products: []
            , firstOpen: true
        }
    }
    , methods: {
        getProducts() {
            if (this.firstOpen) {
                axios.get('http://127.0.0.1:8000/api/products/'
                ).then(response => {
                    this.products = response.data;
                }).catch(err => console.log(err));
            }
            this.firstOpen = false;
        }
        , addProduct(newProduct) {
            this.products.push(newProduct);
            axios.post('http://127.0.0.1:8000/api/products/', newProduct
            ).catch(err => console.log(err));
        }
        , updateProduct(product) {
            axios.put(`http://127.0.0.1:8000/api/products/${product.id}/`, {
                'name': product.name
                , 'description': product.description
            }).catch(err => console.log(err));
        }
        , deleteProduct(id) {
            this.products = this.products.filter(product => product.id !== id);

            axios.delete(`http://127.0.0.1:8000/api/products/${id}/`
            ).catch(err => console.log(err));
        }
        , onProductEdit(id, contentArray) {
            console.log('id>>>', id, '<<<');
            console.log('len>>>', contentArray.length, '<<<');
            console.log('array>>>', contentArray, '<<<');
            console.log('last_element>>>', contentArray[contentArray.length-1], '<<<');

            this.products = this.products.map(function(product) {
                                                    if (product.id === id) {
                                                        product.name = contentArray[0];
                                                        if (contentArray.length > 1) {
                                                            product.description = contentArray[contentArray.length-1];
                                                        }
                                                    }
                                                    return product;
                                                });
        }
    }
}
</script>


<style>
    @import url(https://fonts.googleapis.com/css?family=Roboto:400,300,600,400italic);
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        -webkit-box-sizing: border-box;
        -moz-box-sizing: border-box;
        -webkit-font-smoothing: antialiased;
        -moz-font-smoothing: antialiased;
        -o-font-smoothing: antialiased;
        font-smoothing: antialiased;
        text-rendering: optimizeLegibility;
    }

    body {
        font-family: "Roboto", Helvetica, Arial, sans-serif;
        font-weight: 100;
        font-size: 12px;
        line-height: 30px;
        color: #777;
        background: #4CAF50;
    }

    fieldset {
        border: medium none !important;
        margin: 0 0 10px;
        min-width: 100%;
        padding: 0;
        width: 100%;
    }

    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }

</style>
