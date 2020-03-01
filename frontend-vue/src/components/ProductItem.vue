<template>
    <div class="product-item">
        <br>
        <button v-on:click="$emit('delete-product', product.id)" class="del-btn" title="Delete item">X</button>
        <button v-on:click="$emit('update-product', product)" class="round-btn" title="Update item">U</button>
        <div id="item" contenteditable="true" v-on:blur="onEdit($event, product.id)">
            <h3>{{ product.name }}</h3>
            <h4>{{ product.description }}</h4>
        </div>
    </div>
</template>

<script>
export default {
    name: "ProductItem"
    , props: ["product"]
    , data() {
        return {
            wrongUpdate: false
        }
    }
    , methods: {
        onEdit(evt, id) {
            let contents = evt.target.innerText;
            let contentArray = contents.split("\n");

            if (!contentArray[0]) {
                this.wrongUpdate = true;
                this.$emit('error-msg', 'Name field cannot be empty');
                return;
            }
            else if (this.wrongUpdate) {
                this.wrongUpdate = false;
                this.$emit('error-msg', '');
            }

            this.$emit('on-product-edit', id, contentArray);
        }
    }
}
</script>

<style scoped>
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

    /* .disabled-btn {
        background: #DCDCDC;
        color: white;
        pointer-events: none;
    } */
</style>

