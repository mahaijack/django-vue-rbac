<template>
  <div class="app-container">
    <div style="margin-top:10px">
      <el-input
        v-model="search"
        placeholder="输入角色名称进行搜索"
        style="width: 200px;"
        class="filter-item"
        @keyup.native="handleFilter"
      />
      <el-button type="primary" @click="handleAdd" icon="el-icon-plus">新增</el-button>
    </div>
    <el-table
      :data="tableData"
      stripe
      style="width: 100%;margin-top:10px;"
      v-loading="listLoading"
      border
    >
      <!-- <el-table-column align="center" label="Role Key" width="220">
        <template slot-scope="scope">
          {{ scope.row.id }}
        </template>
      </el-table-column>-->
      <el-table-column align="center" label="角色名称" width="220">
        <template slot-scope="scope">{{ scope.row.name }}</template>
      </el-table-column>
      <el-table-column align="header-center" label="角色描述">
        <template slot-scope="scope">{{ scope.row.desc }}</template>
      </el-table-column>
      <el-table-column align="center" label="操作">
        <template slot-scope="scope">
          <el-button type="primary" size="small" @click="handleEdit(scope)" icon="el-icon-edit"></el-button>
          <el-button type="danger" size="small" @click="handleDelete(scope)" icon="el-icon-delete"></el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog :visible.sync="dialogVisible" :title="dialogType==='edit'?'编辑角色':'新增角色'">
      <el-form :model="role" label-width="80px" label-position="left">
        <el-form-item label="名称">
          <el-input v-model="role.name" placeholder="角色名称" />
        </el-form-item>
        <el-form-item label="描述">
          <el-input
            v-model="role.desc"
            :autosize="{ minRows: 2, maxRows: 4}"
            type="textarea"
            placeholder="角色描述"
          />
        </el-form-item>
        <el-row>
          <el-col :span="12">
            <el-form-item label="数据权限">
              <el-select v-model="role.datas" placeholder="请选择" style="width:90%">
                <el-option
                  v-for="item in dataOptions"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value"
                ></el-option>
              </el-select>
            </el-form-item>
            <el-form-item label="权限范围" v-show="role.datas == '自定义'">
              <el-tree
                class="filter-tree"
                v-model="role.depts"
                :data="orgData"
                show-checkbox
                node-key="id"
                default-expand-all
                highlight-current
                :expand-on-click-node="false"
                ref="depts_tree"
              ></el-tree>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="菜单权限">
              <el-tree
                v-model="role.perms"
                ref="tree"
                :check-strictly="checkStrictly"
                :data="routes"
                show-checkbox
                node-key="id"
                class="permission-tree"
              />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div style="text-align:right;">
        <el-button type="danger" @click="dialogVisible=false">取消</el-button>
        <el-button type="primary" @click="confirmRole">确认</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import path from 'path'
import { genTree, deepClone } from '@/utils'
import {
  getRoutes,
  getRoleAll,
  createRole,
  deleteRole,
  updateRole
} from '@/api/role'
import { getOrgAll } from '@/api/org'

const defaultRole = {
  id: '',
  name: '',
  desc: '',
  perms: [],
  datas: '本级及以下',
  depts: []
};

export default {
  data() {
    return {
      search: '',
      role: Object.assign({}, defaultRole),
      routes: [],
      tableData: [],
      rolesList: [],
      dialogVisible: false,
      dialogType: 'new',
      checkStrictly: true,
      listLoading: true,
      orgData: [],
      dataOptions: [
        {
          value: '全部',
          label: '全部'
        },
        {
          value: '本级',
          label: '本级'
        },
        {
          value: '本级及以下',
          label: '本级及以下'
        },
        {
          value: '仅本人',
          label: '仅本人'
        },
        {
          value: '自定义',
          label: '自定义'
        }
      ]
    }
  },
  computed: {},
  created() {
    // Mock: get all routes and roles list from server
    this.getRoutes()
    this.getOrgAll()
    this.getRoleAll()
  },
  methods: {
    handleFilter() {
      let newData = this.rolesList.filter(
        data =>
          !this.search ||
          data.name.toLowerCase().includes(this.search.toLowerCase())
      );
      this.tableData = genTree(newData)
    },
    async getRoutes() {
      const res = await getRoutes()
      // this.serviceRoutes = res.data
      this.routes = genTree(res.data)
    },
    async getOrgAll() {
      const res = await getOrgAll();
      this.orgData = genTree(res.data)
    },
    async getRoleAll() {
      this.listLoading = true
      const res = await getRoleAll()
      this.tableData = res.data
      this.rolesList = res.data
      this.listLoading = false
    },

    handleAdd() {
      this.role = Object.assign({}, defaultRole);
      if (this.$refs.tree) {
        this.$refs.tree.setCheckedNodes([])
      }
      this.dialogType = 'new'
      this.dialogVisible = true
    },
    handleEdit(scope) {
      this.dialogType = 'edit'
      this.dialogVisible = true
      this.role = deepClone(scope.row)
      this.$nextTick(() => {
        this.$refs.tree.setCheckedKeys(this.role.perms)
        this.$refs.depts_tree.setCheckedKeys(this.role.depts)
      })
    },
    handleDelete({ $index, row }) {
      this.$confirm('确认删除?', '警告', {
        confirmButtonText: '确认',
        cancelButtonText: '取消',
        type: 'warning'
      })
        .then(async () => {
          await deleteRole(row.id)
          this.tableData.splice($index, 1)
          this.$message({
            type: 'success',
            message: '成功删除!'
          })
        })
        .catch(err => {
          console.error(err)
        })
    },

    async confirmRole() {
      const isEdit = this.dialogType === 'edit'
      this.role.perms = this.$refs.tree.getCheckedKeys()
      if (this.role.datas == '自定义') {
        this.role.depts = this.$refs.depts_tree.getCheckedKeys();
      } else {
        this.role.depts = []
      }

      if (isEdit) {
        await updateRole(this.role.id, this.role);
        for (let index = 0; index < this.tableData.length; index++) {
          if (this.tableData[index].id === this.role.id) {
            this.tableData.splice(index, 1, Object.assign({}, this.role))
            break
          }
        }
      } else {
        this.role.perms = this.$refs.tree.getCheckedKeys()
        const { data } = await createRole(this.role)
        this.getRoleAll()
      }

      const { desc, name } = this.role
      this.dialogVisible = false
      this.$notify({
        title: '成功',
        dangerouslyUseHTMLString: true,
        message: `
            <div>角色名: ${name}</div>
            <div>角色描述: ${desc}</div>
          `,
        type: 'success'
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.app-container {
  .roles-table {
    margin-top: 30px;
  }
  .permission-tree {
    margin-bottom: 30px;
  }
}
</style>
