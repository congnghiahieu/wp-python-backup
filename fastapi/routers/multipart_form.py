"""
https://fastapi.tiangolo.com/tutorial/request-files/
 """

from typing import Annotated, Optional, List

from fastapi import APIRouter, File, UploadFile

multipart_form_router = APIRouter(
    prefix="/multipart_form",
    tags=["Multipart Form multipart/form-data"],
)

""" 
Request Files - multipart/form-data

You can define files to be uploaded by the client using:
- File method
or
- UploadFile class

So sánh dùng File method và UploadFile class:
- Giống: Cả 2 sẽ cùng ra 1 giao diện SwaggerUI giống nhau, và cùng 1 document trong OpenAPI giống nhau
- Khác:
    - File() method:
        - File() method sẽ chỉ trả về dạng bytes (1 chuỗi bytes) để mặc cho xử lý tiếp theo (lưu chuỗi bytes đó, ...)
        - File() cũng có validation như Body(), Form(). Chú ý tuy có validation nhưng thường không sử dụng được vì bytes hay gây lỗi decode, encode hơn str, int
    - UploadFile class:
        - Trả về 1 UploadFile instance (đi kèm cùng các attribute, method khác)
        - Không có validation như File(), Body(), Form()
"""


@multipart_form_router.post(
    "/file_method", description="Upload file with File() method"
)
def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@multipart_form_router.post(
    "/uploadfile_class", description="Upload file with UploadFile class"
)
def create_upload_file(file: UploadFile):
    return {
        "filename": file.filename,
        "file_headers": file.headers,
    }


""" Optional File Upload

You can make a file optional by using standard type annotations and setting a default value of None:
"""


@multipart_form_router.post("/files_method_optional")
def create_file_optional(file: Annotated[Optional[bytes], File()] = None):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@multipart_form_router.post("/uploadfile_class_optional")
def create_upload_file_optional(file: Optional[UploadFile] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}


""" UploadFile with Additional Metadata: UploadFile + File() """


@multipart_form_router.post("/uploadfile_file")
def create_uploadfile_class_combine_file_method(
    file: Annotated[UploadFile, File(description="A file would be read as UploadFile")],
):
    return {"filename": file.filename}


""" Multiple File Uploads """


@multipart_form_router.post("/files_multi")
def create_files_multi(files: Annotated[list[bytes], File()]):
    return {"file_sizes": [len(file) for file in files]}


@multipart_form_router.post("/uploadfiles_multi")
def create_upload_files_multi(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}


""" Multiple File Uploads with Additional Metadata """


@multipart_form_router.post("/files_metadata_multi")
def create_files_meta_multi(
    files: Annotated[list[bytes], File(description="Multiple files as bytes")],
):
    return {"total_sizes": sum([len(file) for file in files])}


@multipart_form_router.post("/uploadfiles_metadata_multi")
def create_upload_files_meta_multi(
    files: Annotated[
        list[UploadFile], File(description="Multiple files as UploadFile")
    ],
):
    return {"filenames": [file.filename for file in files]}
