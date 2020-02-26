<template>
    <div class="container" id="contact">
    <form @submit="addProduct"> <!-- action="" method="post"-->
        <h3>Enter info beneath</h3>
        <fieldset>
            <input v-model="prodName" v-bind:placeholder="nameFieldPlaceholder" type="text" tabindex="4" required>
        </fieldset>
        <fieldset>
            <textarea v-model="prodDesc" v-bind:placeholder="descFieldPlaceholder" tabindex="5" required></textarea>
        </fieldset>
        <fieldset>
            <button name="submit" type="submit" id="contact-submit" data-submit="Sending...">Add</button>
        </fieldset>
    </form>
        <button name="show" type="show" id="show" @click="getProducts">{{ showButton }}</button>

        <div class="contents" v-show="!hide">Products:</div>

        <div v-for="product in products" v-bind:key="product.id" v-show="!hide">
            <br>
            <button @click="deleteProduct(product.id)" class="del-btn" title="Delete item">X</button>
            <button @click="updateProduct(product)" class="round-btn" title="Update item">U</button>
            <div id="item" contenteditable="true" @blur="onEdit($event, product.id)">
                <h3>{{ product.name }}</h3>
                <h4>{{ product.description }}</h4>
            </div>
        </div>
    </div>
</template>


<script>

export default {
    name: "Form"
    , data() {
        return {
            changed: true
            , hide: true
            , showButton: 'Show'
            , prodName: ''
            , prodDesc: ''
            , nameFieldPlaceholder: 'Name...'
            , descFieldPlaceholder: 'Description...'
        }
    }
    , props: {
        products: Array
    }
    , methods: {
        getProducts() {
            this.yo = !this.yo;
            if (this.showButton === 'Show') {
                this.hide = false;
                this.showButton = 'Hide';

                if (this.changed) {
                    this.$emit('get-products');
                }
                this.changed = false;
            }
            else {
                this.hide = true;
                this.showButton = 'Show';
            }
        }
        , addProduct(e) {
            e.preventDefault();
            this.changed = true;
            const newProduct = {
                name: this.prodName
                , description: this.prodDesc
            }
           this.$emit('add-product', newProduct);

           this.prodName = '';
           this.prodDesc = '';
           event.currentTarget.reset();
        }
        , deleteProduct(id) {
            this.changed = true;
            this.$emit('delete-product', id);
            this.products = this.products.filter(product => product.id !== id);
        }
        , updateProduct(product) {
            this.changed = true;
            this.$emit('update-product', product);
        }
        , onEdit(evt, id) {
            let contents = evt.target.innerText;
            let contentArray = contents.split("\n");

            for (let i=0; i < this.products.length; ++i) {
                if (this.products[i].id === id) {
                    this.products[i].name = contentArray[0]
                    this.products[i].description = contentArray[contentArray.length-1]
                }
            }
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

    /* .emerge-box { */
        /* opacity: 0; */
        /* animation: fade_in_show 0.5s; */
    /* } */

    .round-btn {
        border: none;
        border-radius: 50%;
        cursor: pointer;
        float: right;
        padding: 5px 9px;
        margin-right: 5px;
    }

    .round-btn:hover {
        background: #28a7fb;
        color: white;
        transition: 0.5s;
    }

    .del-btn {
        border: none;
        border-radius: 50%;
        cursor: pointer;
        float: right;
        padding: 5px 9px;
    }

    .del-btn:hover {
        background: #F74E4E;
        color: white;
        transition: 0.5s;
    }

    .contents {
        text-align: left;
    }

    .container {
        max-width: 400px;
        width: 100%;
        margin: 0 auto;
        position: absolute;
        top: 30%;
        left: 50%;
        -ms-transform: translateX(-50%) translateY(-50%);
        -webkit-transform: translate(-50%,-50%);
        transform: translate(-50%,-50%);
    }


    #contact input[type="text"],
    #contact textarea,
    #contact button[type="submit"] {
        font: 400 12px/16px "Roboto", Helvetica, Arial, sans-serif;
    }
    #contact button[type="show"] {
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
