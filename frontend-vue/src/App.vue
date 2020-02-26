<template>
    <div id="app">
    <!-- <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/about">About</router-link>
    </div> -->
        <Form v-bind:products="products" v-on:get-products="getProducts" v-on:add-product="addProduct"
        v-on:delete-product="deleteProduct" v-on:update-product="updateProduct"/>
    <!-- <router-view/> -->
    </div>
</template>


<script>
import Form from './components/Form'
import axios from 'axios';

export default {
    name: 'app'
    , components: {
        Form
    }
    , data() {
        return {
            products: []
        }
    }
    , methods: {
        getProducts() {
            axios.get('http://127.0.0.1:8000/api/products'
            ).then(response => {
                this.products = response.data;
            }).catch(err => console.log(err));
        }
        , addProduct(newProduct) {
            axios.post('http://127.0.0.1:8000/api/products', newProduct
            ).catch(err => console.log(err));
        }
        , updateProduct(product) {
            axios.put(`http://127.0.0.1:8000/api/products/${product.id}`, {
                'name': product.name
                , 'description': product.description
            }).catch(err => console.log(err));
        }
        , deleteProduct(id) {
            axios.delete(`http://127.0.0.1:8000/api/products/${id}`
            ).catch(err => console.log(err));
        }
    }
}
</script>


<style>
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
