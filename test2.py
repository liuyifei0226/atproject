import atproject.Download.main as at

obj = at.CustomLibrary()

obj.torrent_path = "71e1c9692c556e252aa7e2f4715c419ee447039b.torrent"
path_to_file = obj.get()
print path_to_file