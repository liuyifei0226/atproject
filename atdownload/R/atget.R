#' A Academic Torrent R download function
#'
#' This function allows you to download data through torrent.
#' @param To be added in the future
#' @keywords download
#' @export
#' @examples
#' atget()

atget <- function(name){
       
    script <- paste(system.file(package="atdownload"), "atdownload.py", sep="/")
  	script <- paste(system.file(package="atdownload"), "atdownload.py", sep="/")
  	system2('python',args=c(as.character(script), as.character(name)))
  	
}

