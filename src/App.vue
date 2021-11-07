<template>
  <div id="app">
      <button class="button" @click="CreateMonster">
        モンスターを作成する
      </button>
      <table class="createarea" border="1">
        <select id="select" v-model="monsterselect" v-on:change="SelectMonster">
          <option
            v-for="(monster, key) in monstername"
            v-bind:key="key"
            :value="monster"
          >
            {{ key + ":" + monster }}
          </option>
        </select>
        <tr>
          <td>
            <input
              size="7"
              v-model="name"
              max="7"
              style="font-size: 17px"
              value="ゴブリン"
            />
            hp<input
              type="number"
              min="1"
              max="255"
              v-model="hp"
              size="2"
              style="border-redius: 3px; font-size: 20px"
            />
          </td>
        </tr>
        <tr>
          <td>
            <div
              class="imagedraganddrop"
              @dragenter="DragEnter"
              @dragleave="DragLeave"
              @dragover.prevent
              @drop.prevent="DropFile($event)"
            >
              <br /><br /><img :src="monsterimage" />
            </div>
          </td>
        </tr>
        <tr>
          <td>
            BP:<input
              type="number"
              min="1"
              max="255"
              v-model="bp"
              size="1"
              style="padding: 3px"
            />
            <select id="ability" v-model="ability" @change="AbilitySelect">
              <option
                v-for="(ability, abilityIndex) in abilities"
                v-bind:key="abilityIndex"
              >
                {{ ability.name }}
              </option>
            </select>
          </td>
        </tr>
        <tr>
          <td>
            <textarea class="textarea" :value="abilityEffect"></textarea>
          </td>
        </tr>
      </table>
  </div>
</template>

<script>
import axios from "axios";
axios.defaults.baseURL = "http://localhost:5000";
export default {
  name: "App",
  components: {},
  data() {
    return {
      abilities: [
        { name: "二回行動", effect: "連続二回攻撃できる" },
        { name: "スライムボディ", effect: "たまにダメージを無効化できる" },
        { name: "自然回復", effect: "体の傷がみるみる回復してゆく" },
        { name: "秘めたる力", effect: "5ターンを凌いだら潜在能力を全開する" },
        {
          name: "鼬の最後の屁",
          effect: "致命的な攻撃を耐えきって倍増したパワーで相手に反撃",
        },
        {
          name: "好戦的な性格",
          effect: "ダメージを受ける度に攻撃力がアップする",
        },
        { name: "暗殺の極意", effect: "低確率で相手を一撃で仕留める" },
      ],
      name: "",
      monsterselect: null,
      hp: 0,
      bp: 0,
      abilityindex: 0,
      ability: "",
      abilityEffect: "",
      imagefile: null,
      monsterimage: "",
      isEnter: false,
      monstername: [],
      monsterdata: [],
    };
  },
  mounted() {
    axios.get("/monster").then((data) => {
      console.log(data);
      this.monstername = Object.keys(data["data"]);
      this.monsterdata = data["data"];
      console.log(this.monsterdata);
    });
  },
  methods: {
    AbilitySelect: function () {
      console.log(this.hp);
      this.abilityEffect =
        this.abilities[
          this.abilities.findIndex(({ name }) => name == this.ability)
        ].effect;
      this.abilityindex = document.getElementById("ability").selectedIndex;
      console.log(this.abilityindex);
    },
    CreateMonster: function () {
      axios.post("/monster", {
        param: {
          data: this.monsterdata,
          name: this.name,
          hp: this.hp,
          bp: this.bp,
          ability: this.abilityindex,
        },
      });
    },
    SelectMonster: function () {
      console.log(this.monsterdata[document.getElementById("select").value]);
      this.name = document.getElementById("select").value;
      this.hp = this.monsterdata[document.getElementById("select").value].hp;
      this.bp = this.monsterdata[document.getElementById("select").value].bp;
      this.ability =
        this.abilities[
          this.monsterdata[document.getElementById("select").value].ability
        ].name;
      this.abilityEffect =
        this.abilities[
          this.monsterdata[document.getElementById("select").value].ability
        ].effect;
    },
    DragEnter: function () {
      this.isEnter = true;
    },
    DragLeave: function () {
      this.isEnter = false;
    },
    DropFile(event) {
      let file = event.dataTransfer.files;
      this.imagefile = file;
      this.monsterimage = URL.createObjectURL(this.imagefile[0]);
      this.isEnter = false;
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #0c0c0c;
  margin-top: 60px;
  margin-left: auto;
  margin-right: auto;
}
body {
  background-color: #2c3e50;
}
.button {
  background: #74a15e;
  color: white;
  border: none;
  font-weight: bold;
  font-size: 18px;
  border-radius: 3px;
}
.button:hover {
  background: rgb(136, 62, 136);
}
.createarea {
  border: black solid 5;
  border-width: 5px;
  padding: 0.5em;
  background-color: aliceblue;
  margin: auto;
  font-weight: bold;
  font-size: 23px;
}
.textarea {
  font-size: 23px;
  width: 200px;
  height: 120px;
}
</style>
