## API Documentation

This API allows you to manage guest records in a reservation system.

### Endpoints

- `POST /create` - Create a new guest record.
    - Request body should contain the following fields:
        - `firstname`: First name of the guest.
        - `lastname`: Last name of the guest.
        - `email`: Email address of the guest.
        - `phone`: Phone number of the guest.

- `GET /guests` - Retrieve all guest records.
    - Returns a list of all guest records.

- `GET /guests/{id}` - Retrieve a specific guest record.
    - Path parameter `id` specifies the ID of the guest.
    - Returns the guest record with the specified ID.

- `GET /search` - Search for guest records based on specific criteria.
    - Query parameter `query` specifies the search criteria.
    - Returns a list of guest records that match the search criteria.
    - Supported search criteria include the guest's first name, last name, email, or phone number.

- `PUT /update/{id}` - Update a guest record.
    - Path parameter `id` specifies the ID of the guest to update.
    - Request body should contain the following fields:
        - `firstname`: Updated first name of the guest.
        - `lastname`: Updated last name of the guest.
        - `email`: Updated email address of the guest.
        - `phone`: Updated phone number of the guest.

- `DELETE /delete/{id}` - Delete a guest record.
    - Path parameter `id` specifies the ID of the guest to delete.

### Error Handling

- Error 404: Record not found.
    - If a requested resource or endpoint does not exist, the API will return a JSON response with a 404 status code and a message indicating that the record was not found.

## Contributing

Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
