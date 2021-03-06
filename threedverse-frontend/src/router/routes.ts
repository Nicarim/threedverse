import { RouteConfig } from 'vue-router';

const routes: RouteConfig[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'projects/', component: () => import('pages/ProjectList.vue')},
      { path: 'project/', component: () => import('pages/Project.vue')},
      { path: 'upload/', component: () => import('pages/Upload.vue')}
      ]
  },

];

// Always leave this as last one
if (process.env.MODE !== 'ssr') {
  routes.push({
    path: '*',
    component: () => import('pages/Error404.vue')
  });
}

export default routes;
