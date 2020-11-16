<template>
  <div>
    <form novalidate class="md-layout" @submit.prevent="validateUser" autocomplete="off">
      <md-card class="md-layout-item md-size-50 md-small-size-100">
        <md-card-header>
          <div class="md-title">Login</div>
        </md-card-header>

        <md-card-content>
          <div class="md-layout md-gutter">
            <div class="md-layout-item md-small-size-100">
              <md-field :class="getValidationClass('username')">
                <label for="username">Username</label>
                <md-input name="username" id="username" v-model="loginForm.username" :disabled="sending" autocomplete="off"  />
                <span class="md-error" v-if="!$v.loginForm.username.required">Username is required</span>
                <span class="md-error" v-else-if="!$v.loginForm.username.minlength">Invalid username</span>
              </md-field>
            </div>
          </div>

          <md-field :class="getValidationClass('password')">
            <label for="password">Password</label>
            <md-input type="password" name="password" id="password" v-model="loginForm.password" :disabled="sending" autocomplete="off" />
            <span class="md-error" v-if="!$v.loginForm.password.required">Password is required</span>
            <span class="md-error" v-else-if="!$v.loginForm.password.minlength">Invalid password</span>
          </md-field>
        </md-card-content>

        <md-progress-bar md-mode="indeterminate" v-if="sending" />

        <md-card-actions>
          <md-button type="submit" class="md-primary" :disabled="sending || $v.$invalid">Login</md-button>
        </md-card-actions>
      </md-card>

      <md-snackbar :md-active.sync="userSaved">The user {{ lastUser }} was saved with success!</md-snackbar>
    </form>
  </div>
</template>

<script>
  import { validationMixin } from 'vuelidate'
  import {
    required,
    minLength,
    maxLength
  } from 'vuelidate/lib/validators'
  import senseiService from '@/services/SenseiService'

  export default {
    name: 'Login',
    mixins: [validationMixin],
    data: () => ({
      loginForm: {
        username: null,
        password: null
      },
      userSaved: false,
      sending: false,
      lastUser: null
    }),
    validations: {
      loginForm: {
        username: {
          required,
          minLength: minLength(3)
        },
        password: {
          required,
          minLength: minLength(8)
        }
      }
    },
    methods: {
      getValidationClass (fieldName) {
        const field = this.$v.loginForm[fieldName]

        if (field) {
          return {
            'md-invalid': field.$invalid && field.$dirty
          }
        }
      },
      clearForm () {
        this.$v.$reset()
        this.loginForm.username = null
        this.loginForm.password = null
      },
      authenticateUser () {
        this.sending = true;

        senseiService.authenticate(this.loginForm)
            .then((res) => {
            if(res.data.isValid){
                console.log(res.data.payload)

                this.loginForm.username = "";
                this.loginForm.password = "";
            } else {
                alert(res.data.errorMessage);
            }
            })
            .catch((error) => {
                console.error(error);
            })
            .finally(() => {
                this.sending = false;
                this.clearForm();
            });
      },
      validateUser () {
        this.$v.$touch()

        if (!this.$v.$invalid) {
          this.authenticateUser()
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .md-progress-bar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
  }
</style>