<template>
    <div>
        <button name="show" type="show" id="show" v-on:click="getProducts">{{ showButton }}</button>

        <div class="error-msg" v-show="errorMsg">{{ errorMsg }}</div>
        <div class="contents" v-show="!hide">Products:</div>
        <div v-for="product in products" v-bind:key="product.id" v-show="!hide">
            <ProductItem v-bind:product="product"   v-on:delete-product="(id) => $emit('delete-product', id)"
                                                    v-on:update-product="(product) => $emit('update-product', product)"
                                                    v-on:on-product-edit="(id, contentArray) => $emit('on-product-edit', id, contentArray)"
                                                    v-on:error-msg="function(msg) { errorMsg=''; errorMsg = msg;}"/>
        </div>
    </div>
</template>


<script>
import ProductItem from './ProductItem.vue';

export default {
    name: "Products"
    , components: {
        ProductItem
    }
    , data() {
        return {
            hide: true
            , showButton: 'Show'
            , errorMsg: ''
        }
    }
    , props: {
        products: Array
    }
    , methods: {
        getProducts() {
            if (this.showButton === 'Show') {
                this.$emit('get-products');

                this.hide = false;
                this.showButton = 'Hide';
            }
            else {
                this.errorMsg = '';
                this.hide = true;
                this.showButton = 'Show';
            }
        }
    }
}
</script>


<style>
    /* .emerge-box { */
        /* opacity: 0; */
        /* animation: fade_in_show 0.5s; */
    /* } */

    .error-msg {
        text-align: left;
        color: red;
        font-size: medium;
        background: #FFE5E5;
        animation: blink 0.3s linear 1;
    }

    @keyframes blink{
        0%{opacity: 0;}
        50%{opacity: .5;}
        100%{opacity: 1;}
    }

    .contents {
        text-align: left;
    }

    .container {
        max-width: 400px;
        width: 100%;
        margin: 0 auto;
        position: absolute;
        top: 10%;
        left: 40%;
        /* -ms-transform: translateX(-50%) translateY(-50%); */
        /* -webkit-transform: translate(-50%,-50%); */
        /* transform: translate(-50%,-50%); */
    }

    #contact input[type="text"],
    #contact textarea,
    #contact button[type="submit"] {
        font: 400 12px/16px "Roboto", Helvetica, Arial, sans-serif;
    }

    button[type="show"] {
        font: 400 12px/16px "Roboto", Helvetica, Arial, sans-serif;
    }

    #contact {
        background: #F9F9F9;
        padding: 25px;
        margin: 150px 0;
        box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);
    }

    #contact h3 {
        display: block;
        font-size: 30px;
        font-weight: 300;
        margin-bottom: 10px;
    }

    fieldset {
        border: medium none !important;
        margin: 0 0 10px;
        min-width: 100%;
        padding: 0;
        width: 100%;
    }

    #contact input[type="text"],
    #contact textarea {
        width: 100%;
        border: 1px solid #ccc;
        background: #FFF;
        margin: 0 0 5px;
        padding: 10px;
    }


    #contact input[type="text"]:hover,
    #contact textarea:hover {
        -webkit-transition: border-color 0.3s ease-in-out;
        -moz-transition: border-color 0.3s ease-in-out;
        transition: border-color 0.3s ease-in-out;
        border: 1px solid #aaa;
    }

    #contact textarea {
        height: 100px;
        max-width: 100%;
        resize: none;
    }

    #contact button[type="submit"] {
        cursor: pointer;
        width: 100%;
        border: none;
        background: #4CAF50;
        color: #FFF;
        margin: 0 0 5px;
        padding: 10px;
        font-size: 15px;
    }


    #contact button[type="show"] {
        cursor: pointer;
        width: 100%;
        border: none;
        background: #4CAF50;
        color: #FFF;
        margin: 0 0 5px;
        padding: 10px;
        font-size: 15px;
    }

    #contact button[type="submit"]:hover {
        background: #43A047;
        -webkit-transition: background 0.3s ease-in-out;
        -moz-transition: background 0.3s ease-in-out;
        transition: background-color 0.3s ease-in-out;
    }

    #contact button[type="show"]:hover {
        background: #43A047;
        -webkit-transition: background 0.3s ease-in-out;
        -moz-transition: background 0.3s ease-in-out;
        transition: background-color 0.3s ease-in-out;
    }

    #contact button[type="submit"]:active {
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
    }

    #contact button[type="show"]:active {
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.5);
    }

    .copyright {
        text-align: center;
    }

    #contact input:focus,
    #contact textarea:focus {
        outline: 0;
        border: 1px solid #aaa;
    }

    ::-webkit-input-placeholder {
        color: #888;
    }

    :-moz-placeholder {
        color: #888;
    }

    ::-moz-placeholder {
        color: #888;
    }

    :-ms-input-placeholder {
        color: #888;
    }
</style>
