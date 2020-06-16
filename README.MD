## Djangoのファイル構成
基本的にMVC（DjangoではMTV）アーキテクチャ

### テンプレート(Template)
- htmlファイル
- {{ }}でパラメータを埋め込み

### ビュー(View)
- 処理層
- views.pyに記述
- サーバ内の実際の処理を記述する

### モデル(Model)
- 情報管理層
- models.pyに記述
- データベースの構造を記述する

### ルータ
- urls.pyに記述
- URLの行き先を指定する
