<template>
    <form class="add-product" v-on:submit="addProduct"> <!-- action="" method="post"-->
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
</template>


<script>
export default {
    name: "AddProduct"
    , data() {
        return {
            nameFieldPlaceholder: 'Name...'
            , descFieldPlaceholder: 'Description...'
            , prodName: ''
            , prodDesc: ''
        }
    }
    , methods: {
        addProduct(e) {
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
    }
}
</script>
