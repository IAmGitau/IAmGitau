Vue.component('articles', {
    template:
        `
<div class="lts-msp-art">
    <div class="sn-art" v-for="i in 10">
        <div class="sn-img">
           <slot name="iconImage"></slot>
        </div>
        <div class="sn-art-tl">
             <p>Understanding Default Parameters in JavaScript</p>
        </div>
    </div>
</div>
`
});
new Vue({
    el: ".cly-arc"
});